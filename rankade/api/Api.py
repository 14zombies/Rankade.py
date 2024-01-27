# rankade.api.Api.py
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List, MutableMapping, Optional, TypeAlias, Union

import aiohttp

from .. import RankadeExceptions
from ..Consts import (
    AUTH_ERROR_PREFIX,
    AUTH_ERROR_STATUS,
    DEFAULT_BASE_URL,
    MATCH_ERROR_STATUS,
    MATHC_ERROR_PREFIX,
    QUOTA_ERROR_PREFIX,
    QUOTA_ERROR_STATUS,
)
from ..models import Errors
from .Endpoint import Endpoint, Endpoint_Request
from .RankadeResponse import RankadeResponse
from .Token import Token

logger = logging.getLogger(__name__)

JSON: TypeAlias = Dict[str, "JSON"] | List["JSON"] | str | int | float | bool | None
"""TypeAlias = Dict[str, "JSON"] | List["JSON"] | str | int | float | bool | None"""

HEADERS: TypeAlias = Dict[str, str] | None
"""TypeAlias = Dict[str, str] | None"""

PARAMS: TypeAlias = Dict[str, str | int] | None
"""TypeAlias = Dict[str, str | int] | None"""


@dataclass()
class Api(object):
    """Wrapper around aiohttp.

    It manages the aiohttp ClientSession, Authorisation, and requests to the Rankade API.
    It is generally best to use this as a context manager as it will manage the creation and cleanup of the ClientSession.

    ```python
        async with Api(...) as api:
            result = api.request(...)
    ```
    It can also be used without the context manager, if you are managing the ClientSession & error handling yourself.

    ```python
        api = Api(...)
        async api.start()
        async api.request(...)
        ...
        async api.stop()
    ```
    """

    _base_url: str
    """Scheme and Resource to send requests to. Defaults to "https://api.rankade.com/public/api/1/"""
    _key: Optional[str] = None
    """Rankade key."""
    _secret: Optional[str] = None
    """Rankade secret."""
    _session: Optional[aiohttp.ClientSession] = None
    """aiohttp ClientSession to use, will create one if not passed in.."""
    _token: Optional[Token] = field(init=False, default=None)
    """Rankade issued token"""

    def __init__(
        self,
        key_or_token: str,
        secret: Optional[str] = None,
        base_url: Optional[str] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ):
        """
        :param str key_or_token: Rankade key or token.
        :param Optional[str] secret: Rankade secret.
        :param Optional[str] base_url: Scheme and Resource to send requests to. Defaults to "https://api.rankade.com/public/api/1/"
        :param Optional[aiohttp.ClientSession] session: aiohttp ClientSession to use, will create one if not passed in.
        """
        if not key_or_token or (not isinstance(secret, (str, type(None)))):
            raise RankadeExceptions.NoValidCredentials()
        assert isinstance(base_url, (str, type(None)))
        if secret is not None:
            self._key = key_or_token
            self._secret = secret
        else:
            self.token = key_or_token
        self._base_url = base_url or DEFAULT_BASE_URL
        self._session = session

    @property
    def _credentials_params(self):
        """A dictionary containing the key and secret for Rankade API for use as parameters in the http request."""
        return {"key": self._key, "secret": self._secret}

    @property
    def token(self) -> Optional[Token]:
        """Representation of a JWT."""
        return self._token

    @token.setter
    def token(self, value: Union[str, Token, None]) -> None:
        if isinstance(value, str):
            self._token = Token(token=value)
        else:
            self._token = value

    def _make_url_for(self, endpoint_path: str = "") -> str:
        """
        Returns combined base_url + path for endpoint
        :param str endpoint_path: endpoint path to be turned into full URL.
        """
        endpoint_path = endpoint_path.format(page="", subset="")
        if self._base_url[-1] != "/":
            self._base_url = self._base_url + "/"
        return self._base_url + endpoint_path

    async def _request_jwt(self) -> Optional[Token]:
        """
        Checks whether the token is valid or set and the will grab a new one using the key & secret provided during initialisation.
        :raises NoValidCredentials: If only a token is passed as a parameter to the constructor.
        """
        if self.token is None or self.token.is_invalid:
            if not isinstance(self._key, str) or not isinstance(self._secret, str):
                raise RankadeExceptions.NoValidCredentials("Unable to renew token as no valid key or secret provided.")
            logger.debug("🎟 Requesting new token")
            auth_endpoint = Endpoint_Request(Endpoint.AUTH)
            auth_endpoint.add_parameter("key", self._key)
            auth_endpoint.add_parameter("secret", self._secret)
            token_response = await self._request(endpoint=auth_endpoint)
            self.token = Token(**token_response)

        return self.token

    async def _paginated_request(self, endpoint: Endpoint_Request) -> MutableMapping[str, Any]:
        """
        Loops through the pages of response from the endpoint and combines them all into one Page to return.
        :param Endpoint_Request endpoint: Full information for the request contained in endpoint.Endpoint

        """

        first_page = await self._request(endpoint)
        last_page_no = first_page.get("totalPages", 1)
        # range 2 as already got the first page
        for i in range(2, last_page_no + 1):
            endpoint.page = i
            first_page["page"] = i

            next_page = await self._request(endpoint)
            first_page.get("data", []).extend(next_page.get("data", []))

        return first_page

    async def _request(self, endpoint: Endpoint_Request) -> MutableMapping[str, Any]:
        """
        Main wrapper around aiohttp.ClientSession.request, takes in the Endpoint request transforms it into the appropriate parameters for the ClientSession request.
        :params Endpoint_Request endpoint: full endpoint request.
        """
        if self._session is None:
            raise RankadeExceptions.RankadeException(message="No session set in Api.")
        response = None
        url = self._make_url_for(endpoint.path)
        logger.debug(f"Fetching from: {url}")
        if endpoint.requires_auth:
            self.token = await self._request_jwt()
        if self.token is not None:
            endpoint.add_header("Authorization", self.token.bearer)

        async with self._session.request(
            method=endpoint.method,
            url=url,
            params=endpoint.params,
            headers=endpoint.headers,
            json=endpoint.json,
        ) as raw_response:
            try:
                logger.debug(f"Made request {endpoint} {endpoint.page or ""}")
                response = RankadeResponse(**await raw_response.json())

                # This is response["success"] XOR response["errors"]
                # 1 should be None, if both or neither are then the response is bad.
                assert response.success is not None
                assert response.success != response.errors

                return response.success
            except AssertionError as exp:
                raise await self._exception_of_last_resort(
                    raw_response, message="Unexpected response from Server."
                ) from exp
            except aiohttp.ContentTypeError as exp:
                raise await self._exception_of_last_resort(
                    raw_response, message=f"aiohttp Invalid content type: {raw_response.content_type}."
                ) from exp
            except json.JSONDecodeError as exp:
                raise await self._exception_of_last_resort(raw_response, message="JSON Decoding failed.") from exp

    async def _check_request(self, raw_response: aiohttp.ClientResponse):
        """
        Overrides aiohttp.ClientRequest.raise_for_status to allow better error handling.

        :param aiohttp.ClientResponse raw_response: Client response object.
        :raises ApiErrorResponse: If something unexpected with the response has happened.
        :raises MatchValidation: Match rejected by the server, due to some kind of validation error.
        :raises AuthCredentials: Invalid credentials or client disabled.
        :raises Quotas: One of the quote limits has been hit.
        """
        if raw_response.status == 200:
            return
        response = RankadeResponse(**await raw_response.json())
        if response.errors is None:
            raise await self._exception_of_last_resort(
                response=raw_response, message="No errors returned from server, despite error code."
            )

        errors = Errors.from_dict(data_dict=response.errors)
        if not errors:
            raise await self._exception_of_last_resort(response=raw_response, message="Errors response empty.")

        exception = None
        error_code = errors[0].code
        error_message = errors[0].message
        # Match validation errors have either status code 202 or 400 and have a error code beginning with 'M' folowed by 3 digits.
        if raw_response.status in MATCH_ERROR_STATUS and error_code[0] == MATHC_ERROR_PREFIX:
            exception = RankadeExceptions.MatchValidation
        # Auth Errors will return with status 401 or 403 and have an error code beginning with 'A' folowed by 3 digits.
        elif raw_response.status in AUTH_ERROR_STATUS or error_code[0] == AUTH_ERROR_PREFIX:
            exception = RankadeExceptions.AuthCredentials
        # Quota Errors will a return with status 202 or 429 and have an error code beginning with 'A' folowed by 3 digits.
        # 202 is the general code for Quota errors, however 429 is for Quota & Match Validation errors.
        elif raw_response.status in QUOTA_ERROR_STATUS or error_code[0] == QUOTA_ERROR_PREFIX:
            exception = RankadeExceptions.Quotas
        if exception is None:
            raise await self._exception_of_last_resort(response=raw_response)
        raise exception(
            raw_response.method, raw_response.url.human_repr(), raw_response.status, error_code, error_message
        )

    async def _exception_of_last_resort(
        self,
        response: aiohttp.ClientResponse,
        message: str = "An unknown error occured while dealing with the request.",
    ) -> RankadeExceptions.ApiErrorResponse:
        """
        If something has gone badly wrong with parsing the response, this will create and return an exception to be raised.
        :param aiohttp.ClientResponse response: Response which we are having an issue with.
        :param str message: Message to be added to the exception, will also include the raw text of the response.
        """
        return RankadeExceptions.ApiErrorResponse(
            url=response.url.human_repr(),
            verb=response.method,
            status=response.status,
            message=f"{message} {await response.text()}",
        )

    async def request(
        self,
        endpoint: Endpoint,
        headers: HEADERS = None,
        params: PARAMS = None,
        json: JSON = None,
        **kwargs: Any,
    ) -> MutableMapping[str, Any]:
        """
        Public facing interface for API class, will call 1 of 2 methods depending
        if the request is expecting a paginated response or not.

        :param Endpoint endpoint: Contains basic config for the request, including if authorisation is required, will the response be paginated, and what http method & path to use. See {py:class}`Endpoint <rankade.api.Endpoint.Endpoint>` for a full list.
        :param rankade.api.Api.HEADERS headers: A dict representing any headers to be passed, normally this is internal use only for Bearer Auth header.
        :param rankade.api.Api.PARAMS params: Parameters to use with the request.
        :param rankade.api.Api.JSON json: JSON to send to the server.
        :param **kwargs: Used to keep the call site as clean as possible, we can make almost all the requests with some mix
            of the above parameters. There are a few parameters that require passing through to the request. {py:class}`Endpoint_Request <rankade.api.Endpoint.Endpoint_Request>` for a full list.

        """
        endpoint_request = Endpoint_Request(endpoint=endpoint, headers=headers, params=params, json=json, **kwargs)
        if endpoint_request.is_paginated:
            logger.debug("Endpoint is pageinated.")
            return await self._paginated_request(endpoint_request)
        else:
            logger.debug("Endpoint is not pageinated.")
            return await self._request(endpoint_request)

    def start(self):
        """
        Creates a Client session if none was passed through.

        :::{note}
        Should only be called manually if not using API as a context manager.
        :::
        """
        if self._session is None:
            logger.debug("Creating ClientSession.")
            self._session = aiohttp.ClientSession(raise_for_status=self._check_request)

    async def stop(self):
        """
        Closes the Api session.

        :::{note}
        Should only be called manually if not using API as a context manager.
        :::

        """
        if self._session:
            logger.debug("Closing ClientSession.")
            await self._session.close()

    async def __aenter__(self):
        """Entry handler for context manager."""
        logger.debug("Context started.")
        self.start()
        return self

    async def __aexit__(self, *_):
        """Cleanup handler for context manager."""
        logger.debug("Context finishing.")
        # Do not return 'True' here or exceptions will be supressed.
        # https://docs.python.org/3/reference/datamodel.html?#object.__exit__
        await self.stop()
