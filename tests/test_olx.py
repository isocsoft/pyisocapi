from unittest import IsolatedAsyncioTestCase, mock

from pyisocapi.client import IsocapiClient
from pyisocapi.exceptions import InvalidPageNumberError
from pyisocapi.response import IsocapiAPIResponse
from tests.mocks import mock_valid_request

VALID_OLX_URL_RESPONSE = IsocapiAPIResponse(
    data={"mocked": True}, error="", message="Successfully retrieved data", success=True
)


class TestOLXByURL(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.client = IsocapiClient(api_key="test_api_key")
        return super().setUp()

    @mock.patch("niquests.post", side_effect=mock_valid_request)
    def test_valid(self, _) -> None:
        resp = self.client.get_olx_by_url("https://olx.pl/d/oferta/test.html")
        self.assertEqual(resp, VALID_OLX_URL_RESPONSE)

    @mock.patch("niquests.AsyncSession.post", side_effect=mock_valid_request)
    async def test_valid_async(self, _) -> None:
        resp = await self.client.get_olx_by_url_async(
            "https://olx.pl/d/oferta/test.html"
        )
        self.assertEqual(resp, VALID_OLX_URL_RESPONSE)


class TestOLXByKeyword(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.client = IsocapiClient(api_key="test_api_key")
        return super().setUp()

    @mock.patch("niquests.post", side_effect=mock_valid_request)
    def test_valid(self, _) -> None:
        resp = self.client.get_olx_by_keyword(keyword="iphone", page=1)
        self.assertEqual(resp, VALID_OLX_URL_RESPONSE)

    @mock.patch("niquests.AsyncSession.post", side_effect=mock_valid_request)
    async def test_valid_async(self, _) -> None:
        resp = await self.client.get_olx_by_keyword_async(keyword="iphone", page=1)
        self.assertEqual(resp, VALID_OLX_URL_RESPONSE)

    def test_invalid_page(self) -> None:
        with self.assertRaises(InvalidPageNumberError):
            self.client.get_olx_by_keyword(keyword="iphone", page=0)

    async def test_invalid_page_async(self) -> None:
        with self.assertRaises(InvalidPageNumberError):
            await self.client.get_olx_by_keyword_async(keyword="iphone", page=0)
