from uuid import UUID, uuid4
from dataclasses import dataclass


@dataclass
class Car:
    vin: UUID = uuid4()
    max_current_kw: float
    total_charged_kwh: float = 0.0
