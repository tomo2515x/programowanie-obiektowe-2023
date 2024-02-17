from Charger import Charger
from ChargingService import ChargingService, ClientAccount
from Car import Car
from uuid import uuid4


chargers = [Charger(max_current_kw=10.0), Charger(max_current_kw=15.0)]
service = ChargingService(chargers=chargers)

client_account = ClientAccount(name="John Doe", funds=100)
car = Car(max_current_kw=5.0)
car_2 = Car(max_current_kw=20.0)

service.start_charging(client_account, car, 20, 0)
service.start_charging(client_account, car_2, 50, 1)
service.stop_charging(car)
