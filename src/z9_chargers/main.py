from Charger import Charger
from ChargingService import ChargingService, ClientAccount
from Car import Car


chargers = [Charger(max_current_kw=10.0), Charger(max_current_kw=15.0)]
service = ChargingService(chargers=chargers)

client_account = ClientAccount()
car = Car()
car_2 = Car()

service.start_charging(client_account, car, 20, 0)
service.start_charging(client_account, car_2, 50, 1)
service.stop_charging(car)
