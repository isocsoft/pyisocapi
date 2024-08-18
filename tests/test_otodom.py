from unittest import IsolatedAsyncioTestCase, mock
from pyisocapi.exceptions import (
    InvalidPageNumberError,
)

from .mocks import (
    mock_valid_request,
)
from pyisocapi.client import IsocapiClient
from pyisocapi.payloads import OtodomByKeywordPayload
from pyisocapi.response import IsocapiAPIResponse

VALID_PAYLOAD = OtodomByKeywordPayload(
    page=1,
    voivodeship="mazowieckie",
    city="",
    district="",
    type="",
    transaction_type="",
)


INVALID_PAGE_PAYLOAD = OtodomByKeywordPayload(
    page=0, voivodeship="", city="", district="", type="", transaction_type=""
)

VALID_RESPONSE = IsocapiAPIResponse(
    data={"mocked": True},
    error="",
    message="Successfully retrieved data",
    success=True,
)


class OtodomKeywordTestCase(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.client = IsocapiClient("test_api_key")
        return super().setUp()

    def test_invalid_page(self) -> None:
        with self.assertRaises(InvalidPageNumberError):
            self.client.get_otodom_by_keyword(INVALID_PAGE_PAYLOAD)

    async def test_invalid_page_async(self) -> None:
        with self.assertRaises(InvalidPageNumberError):
            await self.client.get_otodom_by_keyword_async(INVALID_PAGE_PAYLOAD)

    @mock.patch("niquests.post", side_effect=mock_valid_request)
    def test_sync(self, _) -> None:
        resp = self.client.get_otodom_by_keyword(VALID_PAYLOAD)
        self.assertEqual(resp, VALID_RESPONSE)

    @mock.patch("niquests.AsyncSession.post", side_effect=mock_valid_request)
    async def test_async(self, _) -> None:
        resp = await self.client.get_otodom_by_keyword_async(VALID_PAYLOAD)
        self.assertEqual(resp, VALID_RESPONSE)
