# Api.pyi

from asyncio import AbstractEventLoop
from typing import Any, Dict, Optional

from rankade.Errors import Errors
from rankade.ResultList import ResultList
from rankade.TokenAuth import TokenAuth


class Api(object):

    def __init__(self,
                 key_or_token: Optional[str],
                 secret: Optional[str],
                 base_url: Optional[str],
                 loop: Optional[AbstractEventLoop]
                 ) -> None: ...

    async def __aexit__(self, exc_type, exc, tb) -> None: ...

    @property
    def _credentials_params(self) -> Dict[str, str]: ...

    @property
    def token(self) -> TokenAuth: ...

    async def _request_jwt(self, key: str, secret: str) -> Dict[str, str]: ...
    def _make_url_for(self, endpoint: str = ...) -> str: ...

    async def get(self,
                  endpoint: str = ...,
                  params: Optional[Dict[str, str]] = ...,
                  headers: Optional[Dict[str, str]] = ...,
                  json: Optional[Dict[str, Any]] = ...
                  ) -> Dict[str, Any]: ...

    async def post(self,
                   endpoint: str = ...,
                   params: Optional[Dict[str, str]] = ...,
                   headers: Optional[Dict[str, str]] = ...,
                   json: Optional[Dict[str, Any]] = ...
                   ) -> Dict[str, Any]: ...

    async def _request(self,
                       verb: str,
                       endpoint: str = ...,
                       params: Optional[Dict[str, str]] = ...,
                       headers: Optional[Dict[str, str]] = ...,
                       json: Optional[Dict[str, Any]] = ...
                       ) -> Dict[str, Any]: ...

    async def close(self) -> None: ...
