from uuid import UUID, uuid4
from dataclasses import dataclass


@dataclass
class Car:
    max_current_kw: float
    vin: UUID = uuid4()
    total_charged_kwh: float = 0.0
