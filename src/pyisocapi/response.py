from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class IsocapiAPIResponse:
    data: Any
    error: str | list[dict[str, str]]
    message: str
    success: bool
