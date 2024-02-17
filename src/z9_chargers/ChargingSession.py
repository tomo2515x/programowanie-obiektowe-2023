from uuid import uuid4

class ChargingSession:
    def __init__(self, csid, status = "Open"):
        self.status = status
        self.csid = uuid4()
        self.current_kw = 0
        self.total_kwh = 0

    def get_session(self):
        return self.csid
    
    def get_total_kwh(self):
        return self.total_kwh
    
    def get_status(self):
        return self.status
    
    def get_current_kw(self):
        return self.current_kw
    
    def reshuffle_id(self):
        self.csid = uuid4()


