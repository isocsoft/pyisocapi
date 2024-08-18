from dataclasses import dataclass


@dataclass
class OtodomByKeywordPayload:
    page: int

    voivodeship: str
    city: str
    district: str
    type: str
    transaction_type: str

    order_by: str | None = None
    sort_by: str | None = None

    min_price: int | None = None
    max_price: int | None = None
    area_min: int | None = None
    area_max: int | None = None

    min_amount_of_floors: int | None = None
    max_amount_of_floors: int | None = None
    min_price_per_meter: int | None = None
    max_price_per_meter: int | None = None
    days_since_publishing: int | None = None
    build_year_min: int | None = None
    build_year_max: int | None = None

    market_type: str | None = None
    ownership_type: str | None = None
    description_contains: str | None = None

    rooms_amount: list[str] | None = None
    floors: list[str] | None = None
    building_type: list[str] | None = None
    building_materials: list[str] | None = None
    extras: list[str] | None = None
