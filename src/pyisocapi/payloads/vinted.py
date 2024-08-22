from dataclasses import dataclass
from enum import Enum


class CountryCode(str, Enum):
    AUSTRIA = "at"
    BELGIUM = "be"
    CZECHIA = "cz"
    ESTONIA = "ee"
    FRANCE = "fr"
    GERMANY = "de"
    ITALY = "it"
    LATVIA = "lv"
    LITHUANIA = "lt"
    NETHERLANDS = "nl"
    POLAND = "pl"
    SLOVAKIA = "sk"
    SPAIN = "es"
    UNITED_KINGDOM = "co.uk"


@dataclass
class KeywordPayload:
    country_code: CountryCode | str
    keyword: str
    page: int
