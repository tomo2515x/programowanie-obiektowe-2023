class ChargingSession:
    def __init__(self, csid, status = "Open"):
        self.status = status
        self.csid = csid
        self.current_kw = 0
        self.total_kw = 0