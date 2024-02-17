from uuid import UUID


class Car:
    def __init__(self, vin: UUID, total_charged_kwh, max_current_kw):
        self.vin = vin
        self.total_charged_kwh = total_charged_kwh
        self.max_current_kw = max_current_kw
