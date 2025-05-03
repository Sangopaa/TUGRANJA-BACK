from shared.responses.base_response import BaseResponse

from dataclasses import dataclass, field


@dataclass
class DictResponse(BaseResponse):
    status_code: int = 200
    response: dict = field(default_factory=dict)
