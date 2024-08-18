from unittest import TestCase, mock

from pyisocapi.client import IsocapiClient
from pyisocapi.exceptions import (
    BadRequestError,
    InsufficientFundsError,
    InternalServerError,
    RateLimitedError,
    UnknownStatusCodeError,
)

from parameterized import parameterized


class TestResponseExceptionHandler(TestCase):
    def setUp(self) -> None:
        self.client = IsocapiClient("test_api_key")
        return super().setUp()

    @parameterized.expand(
        [
            (200, None, None),
            (400, BadRequestError, "Invalid key"),
            (402, InsufficientFundsError, None),
            (418, UnknownStatusCodeError, None),
            (429, RateLimitedError, None),
            (500, InternalServerError, None),
        ]
    )
    @mock.patch("niquests.Response")
    def test_response_handling(
        self,
        status_code: int,
        expected_exception: type[Exception] | None,
        exception_msg: str | None,
        mock_response: mock.MagicMock,
    ):

        method = getattr(self.client, "_IsocapiClient__response_handling")
        mock_response.status_code = status_code
        if exception_msg:
            mock_response.json.return_value = {"error": exception_msg}

        if expected_exception:
            with self.assertRaises(expected_exception) as e:
                method(mock_response)

            if exception_msg:
                self.assertEqual(str(e.exception), exception_msg)

        else:
            resp = method(mock_response)
            self.assertEqual(resp, mock_response)
