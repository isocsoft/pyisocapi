__BASE_URL = "https://isocapi.com/api/v1"

ISOCAPI_OLX_BY_URL = f"{__BASE_URL}/olx/auction-details-by-url/"
ISOCAPI_OLX_BY_KEYWORD = f"{__BASE_URL}/olx/auctions-details-by-keyword/"
ISOCAPI_OTODOM_BY_KEYWORD = f"{__BASE_URL}/otodom/auctions-details-by-keyword/"

ISOCAPI_API_KEY_HEADER = "X-ISOCAPI-KEY"


UNKNOWN_STATUS_CODE_ERR_MSG = (
    "Unknown status: {} - please open an issue on Github with exception trace."
)
