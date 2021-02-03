# Api.py
import asyncio
import json
import logging

import aiohttp

import rankade.Errors
import rankade.TokenAuth

from . import RankadeExceptions
from .Consts import *


class Api(object):

    def __init__(self, key_or_token=None, secret=None, base_url=DEFAULT_BASE_URL, loop=None):
        self._base_url = base_url
        self._token = None

        if isinstance(secret, str) and isinstance(key_or_token, str):
            self._key = key_or_token
            self._secret = secret
        elif isinstance(key_or_token, str):
            self.token = key_or_token
        else:
            raise RankadeExceptions.NoValidCredentials()
        self.loop = loop or asyncio.get_event_loop()
        self._session = aiohttp.ClientSession(loop=self.loop)

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    @property
    def _credentials_params(self):
        return {"key": self._key, "secret": self._secret}

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = rankade.TokenAuth.TokenAuth(None, value)

    async def _request_jwt(self, key, secret):
        logging.info("Requesting new token")
        token_response = await self.get(
            endpoint="auth",
            params=self._credentials_params
        )
        return token_response

    def _make_url_for(self, endpoint="") -> str:
        return self._base_url + endpoint

    async def get(self, endpoint, params=None, headers=None, json=None):
        return await self._request("GET", endpoint, params, headers, json)

    async def post(self, endpoint, params=None, headers=None, json=None):
        return await self._request("POST", endpoint, params, headers, json)

    async def _request(self, verb, endpoint, params=None, headers=None, json=None):
        url = self._make_url_for(endpoint)
        if DRYRUN:
            if params is None:
                params = dict()
            params["dryrun"] = True
        if "key" not in params and "secret" not in params:
            if self._session.auth is None or self.token.is_invalid:
                self.token = await self._request_jwt(self._key, self._secret)

            headers["Authorization"] = self.token._bearer

        async with self._session.request(
            method=verb,
            url=url,
            params=params,
            headers=headers,
            json=json
        ) as response:
            status = response.status
            try:
                response_json = await response.json()
            except ValueError:
                response_json = {
                    "code": "",
                    "message": "Unable to decode data from server."
                }
            finally:
                await response.release()
            if status == 200:
                return response_json
            elif status in (202, 400, 401, 403, 404, 429, 500):
                errors = rankade.Errors.Errors(
                    self,
                    response_json,
                    response.url,
                    response.method,
                    response.status
                )
                errors.should_raise()
            return response_json

    async def close(self):
        # Remove when aiohttp v4 releases.
        await asyncio.sleep(1)
        await self._session.close()
