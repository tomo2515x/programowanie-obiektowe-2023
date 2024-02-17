from dataclasses import dataclass
from ChargerStatus import ChargerStatus
from uuid import UUID


@dataclass
class Charger:
    max_current_kw: float
    total_charged_kw: float
    attached_car_vin: UUID
    status: ChargerStatus
