# Api.py
import asyncio
import json as js
import logging
from asyncio.events import AbstractEventLoop
from os import error
from typing import Any, Awaitable, Mapping, Optional

import aiohttp
from rankade import RankadeExceptions
from rankade.Consts import DEFAULT_BASE_URL

from ..models import Errors
from ..models.Token import Token
from ..RankadeExceptions import *
from .Endpoint import Endpoint
from .RankadeResponse import RankadeResponse


class Api(object):

    """Api requests class.

    Parameters
    ----------
    key_or_token : :class:`str`
        Rankade key or token.
    secret : :class:`Optional[str]`
        Rankade secret.
    base_url : :class:`str`
        Scheme and Resource to send requests to.
        Defaults to "https://api.rankade.com/public/api/1/"
    loop : :class:`Optional[AbstractEventLoop]`
        asyncio event loop. If not provided will get
        running event loop in the current OS thread.

    Atributes
    ---------

    """
    _key: Optional[str] = None
    _secret: Optional[str] = None
    _base_url: str
    _loop: AbstractEventLoop
    _session: aiohttp.ClientSession
    __token: Optional[Token] = None

    def __init__(self, key_or_token: str, secret: Optional[str] = None, base_url: Optional[str] = None, loop: Optional[asyncio.AbstractEventLoop] = None):
        if not isinstance(key_or_token, (str, type(None))):
            raise RankadeExceptions.NoValidCredentials()
        if not isinstance(secret, (str, type(None))):
            raise RankadeExceptions.NoValidCredentials()
        assert isinstance(base_url, (str, type(None)))
        assert isinstance(loop, (asyncio.AbstractEventLoop, type(None)))

        if secret is not None:
            self._key = key_or_token
            self._secret = secret
        else:
            self._token = key_or_token
        self._base_url = base_url or DEFAULT_BASE_URL
        self._loop = loop or asyncio.get_event_loop()
        self._session = aiohttp.ClientSession(loop=self._loop)

    # Properties
    @property
    def _credentials_params(self):
        return {"key": self._key, "secret": self._secret}

    @property
    def _token(self):
        return self.__token

    @_token.setter
    def _token(self, value):
        if isinstance(value, str):
            self.__token = Token(token=value)
        elif isinstance(value, Token):
            self.__token = value
        else:
            raise Exception

    def _make_url_for(self, endpoint="") -> str:
        endpoint = endpoint.format(page="", subset="")
        if self._base_url[-1] != "/":
            self.base_url = self._base_url + "/"
        return self._base_url + endpoint

    async def _request_jwt(self) -> Optional[Token]:
        if not isinstance(self._key, str) and not isinstance(self._secret, str):
            raise NoValidCredentials("Unable to renew token as no key or secret provided.")
        logging.info("Requesting new token")
        auth_endpoint = Endpoint.AUTH
        auth_endpoint.add_paramater("key", self._key)
        auth_endpoint.add_paramater("secret", self._secret)
        token_response = await self.request(auth_endpoint)
        return Token(**token_response)

    async def _paginated_request(self, endpoint: Endpoint) -> Mapping[str, Any]:
        first_page = await self._request(endpoint)
        last_page_no = first_page.get("totalPages") or 1
        for i in range(2, last_page_no+1):
            endpoint.page = i
            next_page = await self._request(endpoint)
            new_data = next_page.get("data")
            if new_data is None:
                break
            first_page.get("data").extend(new_data)
        return first_page

    async def _request(self, endpoint: Endpoint) -> Mapping[str, Any]:

        url = self._make_url_for(endpoint.path)

        if endpoint.requires_auth:
            if self._token is None or self._token.is_invalid:
                self._token = await self._request_jwt()
            endpoint.add_header("Authorization", self._token._bearer)

        async with self._session.request(
            method=endpoint.method,
            url=url,
            params=endpoint.params,
            headers=endpoint.headers,
            json=endpoint.json
        ) as response:
            status = response.status
            response_object = None
            response_json = None
            try:
                # response_json = await response.json()
                response_json = js.loads(await response.text())
                response_object = RankadeResponse(**response_json)

                # response_json["success"] XOR response_json["errors"]
                # 1 should be None, if both or neither are then bad response.
                assert(response_object.success != response_object.errors)
                assert(status == 200)
                assert(response_object.success is not None)
                return response_object.success

            except (TypeError, ValueError, AssertionError) as e:
                errors_json = {
                    "errors": [{
                        "code": "",
                        "message": "Unable to decode data from server.{}".format(e)
                    }]
                }

                if response_object is not None and response_object.errors is not None:
                    errors_json = response_object.errors
                errors = Errors(
                    self,
                    response.url.human_repr(),
                    response.method,
                    response.status,
                    errors_json
                )
                raise errors.should_raise() or Exception
            finally:
                response.release()

    # Public Api
    def request(self, endpoint: Endpoint) -> Awaitable:
        """Returns Dict[str, Any] or List[Dict[str, Any]"""
        if endpoint.is_paginated:
            return self._paginated_request(endpoint)
        else:
            return self._request(endpoint)

    async def close(self):
        if self._session:
            await self._session.close()
