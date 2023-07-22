class Car:
    def init(self, engine_power, color, acceleration_time, manufacturing_year):
        self.engine_power = engine_power
        self.color = color
        self.acceleration_time = acceleration_time
        self.manufacturing_year = manufacturing_year

class ParkingLot:
    def init(self, capacity, exhibition_year, opening_time, closing_time):
        self.capacity = capacity
        self.exhibition_year = exhibition_year
        self.opening_time = opening_time
        self.closing_time = closing_time

    def park_car(self, car):
        # نحوه پارک کردن ماشین در اینجا پیاده‌سازی می‌شود
        pass

    def unpark_car(self, car):
        # نحوه خروج ماشین از پارکینگ در اینجا پیاده‌سازی می‌شود
        pass

car1 = Car(36000, "آبی", 1.2, 1402)
parking_lot = ParkingLot(120, 1400, "09:00", "20:00")
parking_lot.park_car(car1)