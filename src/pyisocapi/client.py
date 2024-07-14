import niquests


from exceptions import (
    BadRequestError,
    InternalServerError,
    RateLimitedError,
    InsufficientFundsError,
    UnknownStatusCodeError,
    InvalidPageNumberError,
)

from constants import (
    ISOCAPI_OLX_BY_URL,
    ISOCAPI_OLX_BY_QUERY,
    ISOCAPI_API_KEY_HEADER,
    UNKNOWN_STATUS_CODE_ERR_MSG,
)

from response import IsocapiAPIResponse


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

    async def get_old_by_url_async(self, url: str) -> IsocapiAPIResponse:
        async with niquests.AsyncSession() as s:
            resp = await s.post(
                ISOCAPI_OLX_BY_URL,
                json={"url": url},
                headers={ISOCAPI_API_KEY_HEADER: self._api_key},
            )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)

    def get_olx_by_query(self, query: str, page: int) -> IsocapiAPIResponse:
        if page <= 0:
            raise InvalidPageNumberError

        resp = niquests.post(
            ISOCAPI_OLX_BY_QUERY,
            json={"query": query, "page": page},
            headers={ISOCAPI_API_KEY_HEADER: self._api_key},
        )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)

    async def get_old_by_query_async(self, query: str, page: int) -> IsocapiAPIResponse:
        if page <= 0:
            raise InvalidPageNumberError

        async with niquests.AsyncSession() as s:
            resp = await s.post(
                ISOCAPI_OLX_BY_QUERY,
                json={"query": query, "page": page},
                headers={ISOCAPI_API_KEY_HEADER: self._api_key},
            )

        resp = self.__response_handling(resp)
        return self.__niquests_resp_to_isocapi_resp(resp)
