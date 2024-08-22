from unittest import IsolatedAsyncioTestCase, mock

from pyisocapi.client import IsocapiClient
from pyisocapi.exceptions import InvalidPageNumberError
from pyisocapi.payloads.vinted import CountryCode, KeywordPayload
from pyisocapi.response import IsocapiAPIResponse
from tests.mocks import mock_valid_request

VALID_VINTED_URL_RESPONSE = IsocapiAPIResponse(
    data={"mocked": True}, error="", message="Successfully retrieved data", success=True
)

VALID_PAYLOAD = KeywordPayload(
    page=1, keyword="ds2 pants", country_code=CountryCode.POLAND
)
INVALID_PAGE_PAYLOAD = KeywordPayload(
    page=-1, keyword="ds2 pants", country_code=CountryCode.POLAND
)


class TestVintedByKeyword(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.client = IsocapiClient(api_key="test_api_key")
        return super().setUp()

    def test_invalid_page(self) -> None:
        with self.assertRaises(InvalidPageNumberError):
            self.client.get_vinted_by_keyword(INVALID_PAGE_PAYLOAD)

    async def test_invalid_page_async(self) -> None:
        with self.assertRaises(InvalidPageNumberError):
            await self.client.get_vinted_by_keyword_async(INVALID_PAGE_PAYLOAD)

    @mock.patch("niquests.post", side_effect=mock_valid_request)
    def test_valid(self, _) -> None:
        resp = self.client.get_vinted_by_keyword(VALID_PAYLOAD)
        self.assertEqual(resp, VALID_VINTED_URL_RESPONSE)

    @mock.patch("niquests.AsyncSession.post", side_effect=mock_valid_request)
    async def test_valid_async(self, _) -> None:
        resp = await self.client.get_vinted_by_keyword_async(VALID_PAYLOAD)
        self.assertEqual(resp, VALID_VINTED_URL_RESPONSE)
