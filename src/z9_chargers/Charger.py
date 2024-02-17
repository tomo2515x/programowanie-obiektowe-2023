from dataclasses import dataclass
from ChargerStatus import ChargerStatus
from uuid import UUID


@dataclass
class Charger:
    max_current_kw: float
    status: ChargerStatus = ChargerStatus.FREE
    total_charged_kw: float = 0.0
