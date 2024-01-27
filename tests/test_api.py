import json
import unittest
from unittest.mock import AsyncMock, patch

from aioresponses import aioresponses

from rankade.api import Api, Token
from rankade.api.Endpoint import Endpoint, Endpoint_Request
from rankade.Consts import DEFAULT_BASE_URL
from rankade.RankadeExceptions import (
    ApiErrorResponse,
    AuthCredentials,
    MatchValidation,
    NoValidCredentials,
    Quotas,
    RankadeException,
)

from . import consts


class TestApiInit(unittest.TestCase):
    def test_init_with_no_creds(self):
        self.assertRaises(NoValidCredentials, Api, key_or_token="")

    def test_init_with_bad_creds(self):
        self.assertRaises(NoValidCredentials, Api, key_or_token="", secret=42)

    def test_init_with_token(self):
        token = "token"
        api = Api(key_or_token=token)
        self.assertIsInstance(api, Api)
        self.assertIsInstance(api.token, Token)
        self.assertEqual(token, api.token.token)

    def test_init_with_key_and_secret(self):
        key = "key"
        secret = "secret"
        api = Api(key_or_token=key, secret=secret)
        credentials = api._credentials_params
        self.assertEqual(credentials["key"], key)
        self.assertEqual(credentials["secret"], secret)

    def test_init_with_default_url(self):
        api = Api(key_or_token="token")
        self.assertIsInstance(api, Api)
        self.assertEqual(api._base_url, DEFAULT_BASE_URL)

    def test_init_with_custom_url(self):
        url = "https://example.com/"
        api = Api(key_or_token="token", base_url=url)
        self.assertIsInstance(api, Api)
        self.assertEqual(api._base_url, url)

    def test_set_token_with_Token(self):
        token_str = "token"
        token_obj = Token(token=token_str)
        api = Api(key_or_token="not_token")
        api.token = token_obj
        self.assertIsInstance(api.token, Token)
        self.assertEqual(api.token.token, token_str)


class TestApi(unittest.TestCase):
    def test_make_url_for(self):
        token = "token"
        endpoint = Endpoint_Request(Endpoint.AUTH)
        api = Api(key_or_token=token)
        url = api._make_url_for(endpoint_path=endpoint.path)
        self.assertEqual(url, "https://api.rankade.com/public/api/1/auth")

    def test_make_url_for_missing_slash(self):
        token = "token"
        base_url = "https://example.com"
        endpoint = Endpoint_Request(Endpoint.AUTH)
        api = Api(key_or_token=token, base_url=base_url)
        url = api._make_url_for(endpoint_path=endpoint.path)
        self.assertEqual(url, "https://example.com/auth")


class TestApiAsync(unittest.IsolatedAsyncioTestCase):
    @patch(target="rankade.api.Api.Api._request", return_value=consts.token_returnvalue["success"])
    async def test_request_jwt(self, mock_response: AsyncMock):
        key = "key"
        secret = "secret"
        async with Api(key_or_token=key, secret=secret) as api:
            with self.assertLogs(level="DEBUG"):
                api.token = await api._request_jwt()
                mock_response.assert_awaited_once()
                called_params = mock_response.call_args.kwargs["endpoint"].params
                self.assertEqual(called_params["key"], key)
                self.assertEqual(called_params["secret"], secret)
                self.assertEqual(mock_response.call_args.kwargs["endpoint"].endpoint, Endpoint.AUTH)
                self.assertIsInstance(api.token, Token)

    @patch(target="rankade.api.Api.Api._request", return_value=consts.token_returnvalue["success"])
    async def test_request_jwt_bad_key(self, mock_response: AsyncMock):
        async with Api(key_or_token="key", secret="secret") as api:
            api._key = 42
            with self.assertRaises(NoValidCredentials):
                api.token = await api._request_jwt()
            mock_response.assert_not_called()
            mock_response.assert_not_awaited()

    @patch(target="rankade.api.Api.Api._request", return_value=consts.token_returnvalue["success"])
    async def test_request_jwt_bad_secret(self, mock_response: AsyncMock):
        async with Api(key_or_token="key", secret="secret") as api:
            api._secret = 42
            with self.assertRaises(NoValidCredentials):
                api.token = await api._request_jwt()
                mock_response.assert_not_called()

    @patch(target="rankade.api.Api.Api._request", return_value=consts.token_returnvalue["success"])
    async def test_request_with_non_paginated(self, mock_response: AsyncMock):
        async with Api(key_or_token="key", secret="secret") as api:
            endpoint = Endpoint.AUTH
            await api.request(endpoint=endpoint)
            mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._paginated_request", return_value=consts.token_returnvalue["success"])
    async def test_request_with_paginated(self, mock_response: AsyncMock):
        async with Api(key_or_token="key", secret="secret") as api:
            endpoint = Endpoint.PLAYERS
            await api.request(endpoint=endpoint)
            mock_response.assert_awaited_once()

    @aioresponses()
    async def test_paginated_request(self, mock_response: aioresponses):
        token = consts.make_token(consts.valid_token_message)
        url_1 = f"{consts.base_url}matches/1"
        url_2 = f"{consts.base_url}matches/2"
        mock_response.get(url=url_1, body=json.dumps(consts.matches_returnvalue_page_1))
        mock_response.get(url=url_2, body=json.dumps(consts.matches_returnvalue_page_2))

        async with Api(key_or_token=token) as api:
            endpoint = Endpoint_Request(Endpoint.MATCHES)
            result = await api._paginated_request(endpoint=endpoint)
            # self.assertEqual(mock_response.call_count, 2)
            self.assertEqual(len(result["data"]), 6)

    @aioresponses()
    async def test__request(self, mock_response: aioresponses):
        url = f"{consts.base_url}auth"
        status = 200
        body = json.dumps(consts.token_returnvalue)

        mock_response.get(
            url=url,
            status=status,
            body=body,
        )
        async with Api(key_or_token="key", secret="secret") as api:
            endpoint = Endpoint_Request(Endpoint.AUTH)
            result = await api._request(endpoint=endpoint)
            mock_response.assert_any_call(url)
            self.assertEqual(result, consts.token_returnvalue["success"])

    @aioresponses()
    async def test__request_with_no_session(self, mock_response: aioresponses):
        url = f"{consts.base_url}auth"
        status = 200
        body = json.dumps(consts.token_returnvalue)

        mock_response.get(
            url=url,
            status=status,
            body=body,
        )
        async with Api(key_or_token="key", secret="secret") as api:
            endpoint = Endpoint_Request(Endpoint.AUTH)
            # Close session to prevent warning, before setting _session to None.
            await api._session.close()
            api._session = None
            with self.assertRaises(RankadeException):
                await api._request(endpoint=endpoint)

    @aioresponses()
    async def test__request_with_auth(self, mock_response: aioresponses):
        key = "key"
        secret = "secret"
        auth_url = f"{consts.base_url}auth?key={key}&secret={secret}"
        quota_url = f"{consts.base_url}quota"

        status = 200
        auth_body = json.dumps(consts.token_returnvalue)
        quota_body = json.dumps(consts.quota_returnvalue)

        mock_response.get(url=auth_url, status=status, body=auth_body)
        mock_response.get(url=quota_url, status=status, body=quota_body)
        async with Api(key_or_token=key, secret=secret) as api:
            endpoint = Endpoint_Request(Endpoint.QUOTA)
            result = await api._request(endpoint=endpoint)
            mock_response.assert_any_call(auth_url)
            mock_response.assert_any_call(quota_url)
            self.assertEqual(result, consts.quota_returnvalue["success"])

    # Passes with patched version of aioresponses until PR 251 is merged.
    # https://github.com/pnuckowski/aioresponses/pull/251/
    @aioresponses()
    async def test__request_with_status_error(self, mock_response: aioresponses):
        key = "key"
        secret = "secret"
        url = f"https://api.rankade.com/public/api/1/test"
        status = 401
        body = json.dumps(consts.errors_returnvalue)
        mock_response.get(url=url, status=status, body=body)
        async with Api(key_or_token=key, secret=secret) as api:
            endpoint = Endpoint_Request(endpoint=Endpoint._TEST)
            with self.assertRaises(AuthCredentials):
                await api._request(endpoint=endpoint)


class TestRaises(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        token = consts.make_token(consts.valid_token_message)
        self.api = Api(key_or_token=token)

    @aioresponses()
    async def test_raises_ApiErrorResponse(self, mock_response: aioresponses):
        mock_response.get(url=f"{consts.base_url}test", body=json.dumps({"success": {}, "errors": {}}))
        with self.assertRaises(ApiErrorResponse) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual('Unexpected response from Server. {"success": {}, "errors": {}}', exception.exception.message)
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_ContentTypeError(self, mock_response: aioresponses):
        mock_response.get(url=f"{consts.base_url}test", content_type="video/mpeg")
        with self.assertRaises(ApiErrorResponse) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual("aiohttp Invalid content type: video/mpeg. ", exception.exception.message)
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_JSONDecodeError(self, mock_response: aioresponses):
        mock_response.get(url=f"{consts.base_url}test", body="{ 'foo': {}")
        with self.assertRaises(ApiErrorResponse) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual("JSON Decoding failed. { 'foo': {}", exception.exception.message)
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_not_200_errors_none(self, mock_response: aioresponses):
        mock_response.get(url=f"{consts.base_url}test", status=201, body=json.dumps(consts.quota_returnvalue))
        with self.assertRaises(ApiErrorResponse) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual(
            f"No errors returned from server, despite error code. {json.dumps(consts.quota_returnvalue)}",
            exception.exception.message,
        )
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_not_200_no_errors(self, mock_response: aioresponses):
        mock_response.get(url=f"{consts.base_url}test", status=201, body='{"errors":[]}')
        with self.assertRaises(ApiErrorResponse) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual(
            'Errors response empty. {"errors":[]}',
            exception.exception.message,
        )
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_400_M001(self, mock_response: aioresponses):
        mock_response.get(
            url=f"{consts.base_url}test", status=400, body=json.dumps(consts.errors_match_validation_400_M001)
        )
        with self.assertRaises(MatchValidation) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual(
            "Invalid JSON message in request.",
            exception.exception.message,
        )
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_201_M002(self, mock_response: aioresponses):
        mock_response.get(
            url=f"{consts.base_url}test", status=400, body=json.dumps(consts.errors_match_validation_202_M002)
        )
        with self.assertRaises(MatchValidation) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual(
            "JSON schema validation error.",
            exception.exception.message,
        )
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_401_A001(self, mock_response: aioresponses):
        mock_response.get(
            url=f"{consts.base_url}test", status=401, body=json.dumps(consts.errors_match_validation_401_A001)
        )
        with self.assertRaises(AuthCredentials) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual(
            "Invalid credentials or client disabled.",
            exception.exception.message,
        )
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_403_A001(self, mock_response: aioresponses):
        mock_response.get(
            url=f"{consts.base_url}test", status=403, body=json.dumps(consts.errors_match_validation_401_A001)
        )
        with self.assertRaises(AuthCredentials) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual(
            "Invalid credentials or client disabled.",
            exception.exception.message,
        )
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_202_Q001(self, mock_response: aioresponses):
        mock_response.get(
            url=f"{consts.base_url}test", status=202, body=json.dumps(consts.errors_match_validation_429_Q001)
        )
        with self.assertRaises(Quotas) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual(
            "API calls per year limit has been reached.",
            exception.exception.message,
        )
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_429_Q001(self, mock_response: aioresponses):
        mock_response.get(
            url=f"{consts.base_url}test", status=429, body=json.dumps(consts.errors_match_validation_429_Q001)
        )
        with self.assertRaises(Quotas) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual(
            "API calls per year limit has been reached.",
            exception.exception.message,
        )
        mock_response.assert_called_once()

    @aioresponses()
    async def test_raises_500(self, mock_response: aioresponses):
        mock_response.get(
            url=f"{consts.base_url}test", status=500, body=json.dumps(consts.errors_match_validation_500_R001)
        )
        with self.assertRaises(ApiErrorResponse) as exception:
            async with self.api as api:
                result = await api.request(Endpoint._TEST)
        self.assertEqual(
            'An unknown error occured while dealing with the request. {"errors": [{"code": "R001", "message": "Generic error."}]}',
            exception.exception.message,
        )
        mock_response.assert_called_once()


if __name__ == "__main__":
    unittest.main()
