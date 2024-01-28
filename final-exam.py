##Bai1

class Car:
    def __init__(self):
        self.open = False

    def open_door(self):
        self.open = True

    def close_door(self):
        self.open = False


class Motorcycle:
    def __init__(self):
        self.stand_out = False


class Vehicle(Car, Motorcycle):
    def __init__(self):
        Car.__init__(self)
        Motorcycle.__init__(self)
        self.started = False
        self.speed = 0

    def start(self):
        self.started = True

    def set_speed(self, value):
        self.speed = value

    def display_info(self):
        car_info = f"Trạng thái cửa xe: {'Mở' if self.open else 'Đóng'}"
        motorcycle_info = f"Trạng thái xe moto: {'Di chuyển' if self.stand_out else 'Dừng lại'}"
        vehicle_info = f"Trạng thái của phương tiện:  {'Di chuyển' if self.started else 'Dừng lại'}, Tốc độ: {self.speed} km/h"

        print(car_info)
        print(motorcycle_info)
        print(vehicle_info)


vehicle = Vehicle()

car_door_input = input("Cửa xe có đang mở không? (Có/Không): ")
if car_door_input.lower() == 'có':
    vehicle.open_door()

motorcycle_stand_input = input("Phương tiện có đang di chuyển không? (Có/Không): ")
if motorcycle_stand_input.lower() == 'có':
    vehicle.stand_out = True
    vehicle.start()

speed_input = input("Tốc độ di chuyển của phương tiện (km/h): ")

vehicle.set_speed(int(speed_input))
vehicle.display_info()


#Bai2
#2.1
tuple_example = ('a', 2, 'c', 4, 6, 8)
max_value = max([i for i in tuple_example if isinstance(i, int)])
min_value = min([i for i in tuple_example if isinstance(i, int)])
print("Max value: ", max_value)
print("Min value:", min_value)
#2.2
tuple2 = ('d', 1, 'e', 3, 5, 7, 9)

tuple2_inverted = tuple2[::-1]

print("Reversed tuple:", tuple2_inverted)

#2.3
tuple1 = ('a', 2, 'c', 4, 6, 8)
tuple2 = ('d', 1, 'e', 3, 5, 7, 9)

tuple3 = tuple1 + tuple2

print("Tuple3:", tuple3)

#2.4
tuple2 = ('d', 1, 'e', 3, 5, 7, 9)

value_at_index_5 = tuple2[5]

print("Value at index 5:", value_at_index_5)

#3





