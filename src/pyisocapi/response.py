from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class IsocapiAPIResponse:
    data: Any
    error: str
    message: str
    success: bool
