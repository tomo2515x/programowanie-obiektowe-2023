from enum import Enum


class ChargingStatus(Enum):
    OPEN = 0
    ERROR = 1
    FINISHED = 2