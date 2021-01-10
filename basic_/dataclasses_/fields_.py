from dataclasses import dataclass, fields, field
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class SnowCreateResponse:
    transactionid: str
    created: Optional[str]
    message_sent: Optional[str]
    valid: Optional[bool]
    error: Optional[str]
    transform_link: Optional[str]
    target_link: Optional[str]
    ui_link: Optional[str]
    task_link: Optional[str]
    ui_task_link: Optional[str]
    wi_link: Optional[str]
    wi_ui_link: Optional[str]
    number: Optional[str] = field(init=False, default=None)

    def __post_init__(self):
        if self.transactionid is None:
            raise Exception("Field `transactionid` is null")

    @classmethod
    def fields(cls):
        return [f.name for f in fields(cls)]




print(SnowCreateResponse.fields())
print(SnowCreateResponse.field())
print(SnowCreateResponse().props())
