import dataclasses
import niquests


from .exceptions import (
    BadRequestError,
    InternalServerError,
    RateLimitedError,
    InsufficientFundsError,
    UnknownStatusCodeError,
    InvalidPageNumberError,
)

from .constants import (
    ISOCAPI_OLX_BY_URL,
    ISOCAPI_OLX_BY_KEYWORD,
    ISOCAPI_API_KEY_HEADER,
    ISOCAPI_OTODOM_BY_KEYWORD,
    ISOCAPI_VINTED_BY_KEYWORD,
    UNKNOWN_STATUS_CODE_ERR_MSG,
)

from .payloads.otodom import KeywordPayload as OtodomByKeywordPayload
from .payloads.vinted import KeywordPayload as VintedByKeywordPayload
from .response import IsocapiAPIResponse


class IsocapiClient:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def __niquests_resp_to_isocapi_resp(
        self, niquest_response: niquests.Response
    ) -> IsocapiAPIResponse:
        try:
            json_response = niquest_response.json()
        except niquests.JSONDecodeError:
            raise InternalServerError

        return IsocapiAPIResponse(
            data=json_response["data"],
            error=json_response["error"],
            message=json_response["message"],
            success=json_response["success"],
        )

    def __get_bad_request_msg_from_response(self, response: niquests.Response) -> str:
        try:
            return response.json()["error"]
        except niquests.JSONDecodeError:
            raise InternalServerError

    def __response_handling(
        self,
        resp: niquests.Response,
    ) -> niquests.Response:
        match resp.status_code:
            case 200:
                return resp
            case 400:
                raise BadRequestError(self.__get_bad_request_msg_from_response(resp))
            case 402:
                raise InsufficientFundsError
            case 429:
                raise RateLimitedError
            case 500:
                raise InternalServerError
            case _:
                raise UnknownStatusCodeError(
                    UNKNOWN_STATUS_CODE_ERR_MSG.format(resp.status_code)
                )

    def get_olx_by_url(self, url: str) -> IsocapiAPIResponse:
        resp = niquests.post(
            ISOCAPI_OLX_BY_URL,
            json={"url": url},
            headers={ISOCAPI_API_KEY_HEADER: self._api_key},
        )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)

    async def get_olx_by_url_async(self, url: str) -> IsocapiAPIResponse:
        async with niquests.AsyncSession() as s:
            resp = await s.post(
                ISOCAPI_OLX_BY_URL,
                json={"url": url},
                headers={ISOCAPI_API_KEY_HEADER: self._api_key},
            )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)

    def get_olx_by_keyword(self, keyword: str, page: int) -> IsocapiAPIResponse:
        if page <= 0:
            raise InvalidPageNumberError

        resp = niquests.post(
            ISOCAPI_OLX_BY_KEYWORD,
            json={"query": keyword, "page": page},
            headers={ISOCAPI_API_KEY_HEADER: self._api_key},
        )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)

    async def get_olx_by_keyword_async(
        self, keyword: str, page: int
    ) -> IsocapiAPIResponse:
        if page <= 0:
            raise InvalidPageNumberError

        async with niquests.AsyncSession() as s:
            resp = await s.post(
                ISOCAPI_OLX_BY_KEYWORD,
                json={"query": keyword, "page": page},
                headers={ISOCAPI_API_KEY_HEADER: self._api_key},
            )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)

    def get_otodom_by_keyword(
        self, payload: OtodomByKeywordPayload
    ) -> IsocapiAPIResponse:
        if payload.page <= 0:
            raise InvalidPageNumberError

        resp = niquests.post(
            ISOCAPI_OTODOM_BY_KEYWORD,
            json=dataclasses.asdict(payload),
            headers={ISOCAPI_API_KEY_HEADER: self._api_key},
        )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)

    async def get_otodom_by_keyword_async(
        self, payload: OtodomByKeywordPayload
    ) -> IsocapiAPIResponse:
        if payload.page <= 0:
            raise InvalidPageNumberError

        async with niquests.AsyncSession() as s:
            resp = await s.post(
                ISOCAPI_OTODOM_BY_KEYWORD,
                json=dataclasses.asdict(payload),
                headers={ISOCAPI_API_KEY_HEADER: self._api_key},
            )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)

    def get_vinted_by_keyword(
        self, payload: VintedByKeywordPayload
    ) -> IsocapiAPIResponse:
        if payload.page <= 0:
            raise InvalidPageNumberError

        resp = niquests.post(
            ISOCAPI_VINTED_BY_KEYWORD,
            json={
                "page": payload.page,
                "keyword": payload.keyword,
                "countryCode": payload.country_code,
            },
            headers={ISOCAPI_API_KEY_HEADER: self._api_key},
        )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)

    async def get_vinted_by_keyword_async(
        self, payload: VintedByKeywordPayload
    ) -> IsocapiAPIResponse:
        if payload.page <= 0:
            raise InvalidPageNumberError

        async with niquests.AsyncSession() as s:
            resp = await s.post(
                ISOCAPI_VINTED_BY_KEYWORD,
                json={
                    "page": payload.page,
                    "keyword": payload.keyword,
                    "countryCode": payload.country_code,
                },
                headers={ISOCAPI_API_KEY_HEADER: self._api_key},
            )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)
