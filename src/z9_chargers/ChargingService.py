import Car, ChargingSession, Charger
from uuid import uuid4

class ClientAccount:
    def __init__(self, id ,name , funds):
        self.id = id
        self.name = name
        self.funds = funds
        
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
        #should it be zero?
        self.chargers = chargers
        self.time_modifier = time_modifier

    def start_charging(client_id, vim, kwh, desired_current_kw, charger_position: int):
            #start charging session, check current, adjust if needed
        

