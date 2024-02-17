from Car import Car
from Charger import Charger
from uuid import uuid4, UUID
from dataclasses import dataclass


@dataclass
class ClientAccount:
    name: str
    funds: int
    id: UUID = uuid4()

    def get_funds(self):
        return self.funds

    def insert_funds(self, amount):
        self.funds = self.funds + amount
        return self.funds

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class ChargingService:
    def __init__(self, chargers: list[Charger], time_modifier: float = 0):
        # should it be zero?
        self.chargers = chargers
        self.time_modifier = time_modifier

    def start_charging(
        self, account: ClientAccount, car: Car, how_much: int, charger_position: int
    ):
        print(
            f"Charging on account ({account.id}), car id ({car.id}), will change {how_much}kWh on position {charger_position}"
        )

    def stop_charging(self, car):
        # stop it, yank the cable
        pass

    def attach_charger(charger):
        # shouldit be called after or before starting???
        pass

    def remove_charger(charger):
        # unplug :3
        pass

    def disable_charger(charger_position: int):
        # disables charger??/ like when and why? powersaving lmao
        pass

    def enable_charger(charger_position: int):
        # does the same but opposite
        pass
