from uuid import uuid4

class ChargingSession:
    def __init__(self, csid, status = "Open"):
        self.status = status
        self.csid = uuid4()
        self.current_kw = 0
        self.total_kwh = 0


