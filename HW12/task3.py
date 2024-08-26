class Bus:
    def __init__(self, max_speed, max_seats):
        self.speed = 0
        self.max_speed = max_speed
        self.max_seats = max_seats
        self.passengers = []
        self.free_seats = max_seats
        self.seats = {i: None for i in range(1, max_seats + 1)}

    def boarding(self, *passengers):
        for passenger in passengers:
            if self.free_seats > 0:
                self.passengers.append(passenger)
                self.free_seats -= 1
                for seat, name in self.seats.items():
                    if name is None:
                        self.seats[seat] = passenger
                        break
            else:
                print("No free seats!")

    def getting_off(self, *passengers):
        for passenger in passengers:
            if passenger in self.passengers:
                self.passengers.remove(passenger)
                self.free_seats += 1
                for seat, name in self.seats.items():
                    if name == passenger:
                        self.seats[seat] = None
                        break
            else:
                print(f"Passanger {passenger} not in the bus.")

    def speed(self, value):
        self.speed = min(self.speed + value, self.max_speed)

    def brakes(self, value):
        self.speed = max(self.speed - value, 0)

    def __contains__(self, passenger):
        return passenger in self.passengers

    def __iadd__(self, passenger):
        self.boarding(passenger)
        return self

    def __isub__(self, passenger):
        self.getting_off(passenger)
        return self


bus = Bus(100, 5)
bus.boarding("Иванов", "Петров", "Сидоров")
print(bus.passengers)  # Выведет ['Иванов', 'Петров', 'Сидоров']
print("Петров" in bus)  # Выведет True
bus += "Козлов"
bus -= "Петров"
print(bus.passengers)
