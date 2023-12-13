class Display():
    def __init__(self, id, message, is_on, car_park):
        self.id = id
        self.message = ""
        self.is_on = False
        self.car_park = car_park
        
    def __str__(self):
        return "Display 1: Welcome to the automated car park"
        
        
        
