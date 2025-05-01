from typing import Any
from abc import ABC

from dataclasses import dataclass


@dataclass
class BaseResponse(ABC):
    status_code: int
    response: Any
