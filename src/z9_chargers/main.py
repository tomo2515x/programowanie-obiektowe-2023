from Charger import Charger
from ChargingService import ChargingService, ClientAccount
from Car import Car


chargers = [Charger(), Charger()]
service = ChargingService()

client_account = ClientAccount()
car = Car()
car_2 = Car()

service.start_charging(client_account, car, 20, 0)
service.start_charging(client_account, car_2, 50, 1)
service.stop_charging(car)
