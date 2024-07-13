__BASE_URL = "https://isocapi.com/api/v1"

ISOCAPI_OLX_BY_URL = f"{__BASE_URL}/olx/url/"
ISOCAPI_OLX_BY_QUERY = f"{__BASE_URL}/olx/query/"


ISOCAPI_API_KEY_HEADER = "X-ISOCAPI-KEY"


OLX_BY_URL_BAD_URL_PASSED_ERR_MSG = (
    lambda url: f"Passed URL - {url} - is in invalid format"
)


UNKNOWN_STATUS_CODE_ERR_MSG = (
    "Unknown status: {} - please open an issue on Github with exception trace."
)