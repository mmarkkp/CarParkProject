from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from sensor import Sensor

class main:

    my_car_park = CarPark("Moondalup", 100, "moondalup.txt")
    my_entry_sensor = EntrySensor(1, True, "car_park")
    my_exit_sensor = ExitSensor(2, True, "car_park")
    my_display = Display(1, "Welcome To Moondalup", True, "car_park")
    print(EntrySensor(5, 10, True))
    print(ExitSensor(5, 2, True))


    print(my_car_park.location)
    print(my_car_park.capacity)
    print(my_car_park.log_file)
    print(my_entry_sensor.id)
    print(my_entry_sensor.is_active)
    print(my_entry_sensor.car_park)
    print(my_exit_sensor.id)
    print(my_exit_sensor.is_active)
    print(my_exit_sensor.car_park)
    print(my_display.id)
    print(my_display.message)
    print(my_display.is_on)
    print(my_display.car_park)

if __name__ == '__main__':
    main()

      