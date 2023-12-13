class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors or []
        self.displays = displays
        
    