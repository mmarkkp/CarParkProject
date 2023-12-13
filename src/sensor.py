class Sensor:
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = False
        self.car_park = car_park
        
    def _str__(self):
        return f'The sensors id is: {self.id} and the status is: {self.is_active}'
    
class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    pass
