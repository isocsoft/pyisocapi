from dataclasses import dataclass
from enum import IntEnum, StrEnum


class Voivodeship(StrEnum):
    DOLNOSLASKIE = "dolnoslaskie"
    KUJAWSKO_POMORSKIE = "kujawsko-pomorskie"
    LODZKIE = "lodzkie"
    LUBELSKIE = "lubelskie"
    LUBUSKIE = "lubuskie"
    MALOPOLSKIE = "malopolskie"
    MAZOWIECKIE = "mazowieckie"
    OPOLSKIE = "opolskie"
    PODKARPACKIE = "podkarpackie"
    PODLASKIE = "podlaskie"
    POMORSKIE = "pomorskie"
    SLASKIE = "slaskie"
    SWIETOKRZYSKIE = "swietokrzyskie"
    WARMINSKO_MAZURSKIE = "warminsko-mazurskie"
    WIELKOPOLSKIE = "wielkopolskie"
    ZACHODNIOPOMORSKIE = "zachodniopomorskie"


class Type(StrEnum):
    APARTMENT = "mieszkanie"
    STUDIO = "kawalerka"
    HOUSE = "dom"
    INVESTMENT = "inwestycja"
    ROOM = "pokoj"
    PLOT = "dzialka"
    PREMISES = "lokal"
    WAREHOUSE = "haleimagazyny"
    GARAGE = "garaz"


class TransactionType(StrEnum):
    SALE = "sprzedaz"
    RENT = "wynajem"


class OrderBy(StrEnum):
    ASC = "asc"
    DESC = "desc"


class SortBy(StrEnum):
    AREA = "area"
    LATEST = "latest"
    PRICE = "price"


class DaysSincePublishing(IntEnum):
    ONE = 1
    THREE = 3
    SEVEN = 7


class MarketType(StrEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class OwnershipType(StrEnum):
    ALL = "all"
    DEVELOPER = "developer"
    AGENCY = "agency"
    PRIVATE = "private"


class RoomsAmount(StrEnum):
    ONE = "one"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"
    SIX_PLUS = "six_plus"


class Floors(StrEnum):
    CELLAR = "cellar"
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"
    FOURTH = "fourth"
    FIFTH = "fifth"
    SIXTH = "sixth"
    SEVENTH = "seventh"
    EIGHTH = "eighth"
    NINTH = "ninth"
    TENTH = "tenth"
    TENTH_PLUS = "tenth_plus"
    GARRET = "garret"


class BuildingType(StrEnum):
    BLOCK = "block"
    TENEMENT = "tenement"
    HOUSE = "house"
    INFILL = "infill"
    RIBBON = "ribbon"
    APARTMENT = "apartment"
    LOFT = "loft"


class BuildingMaterials(StrEnum):
    BRICK = "brick"
    WOOD = "wood"
    BREEZE_BLOCK = "breezeblock"
    HYDROTON = "hydroton"
    CONCRETE_PLATE = "concrete_plate"
    CONCRETE = "concrete"
    SILIKAT = "silikat"
    CELLULAR_CONCRETE = "cellular_concrete"
    OTHER = "other"
    REINFORCED_CONCRETE = "reinforced_concrete"


class Extras(StrEnum):
    TERRACE = "terrace"
    BALCONY = "balcony"
    GARAGE = "garage"
    BASEMENT = "basement"
    LIFT = "lift"
    HAS_PHOTOS = "has_photos"
    TWO_STORY = "two_story"
    GARDEN = "garden"
    SEPARATE_KITCHEN = "separate_kitchen"


@dataclass
class KeywordPayload:
    page: int

    voivodeship: Voivodeship
    city: str
    district: str
    type: Type
    transaction_type: TransactionType

    order_by: OrderBy | None = None
    sort_by: SortBy | None = None

    min_price: int | None = None
    max_price: int | None = None
    area_min: int | None = None
    area_max: int | None = None

    min_amount_of_floors: int | None = None
    max_amount_of_floors: int | None = None
    min_price_per_meter: int | None = None
    max_price_per_meter: int | None = None
    days_since_publishing: DaysSincePublishing | None = None
    build_year_min: int | None = None
    build_year_max: int | None = None

    market_type: MarketType | None = None
    ownership_type: OwnershipType | None = None
    description_contains: str | None = None

    rooms_amount: list[RoomsAmount] | None = None
    floors: list[Floors] | None = None
    building_type: list[BuildingType] | None = None
    building_materials: list[BuildingMaterials] | None = None
    extras: list[Extras] | None = None
