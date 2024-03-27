import random


class Object:
    __ID_LIST = list(range(1, 201))
    random.shuffle(__ID_LIST)

    __COUNTER: int = 0
    """
    fuel_volume
    number_of_parking_days
    current_parking_day
    position
    current_position
    """

    def __init__(self, number: int = 1, current: int = 2, fuel: float = 0):
        if self.checking_in_interval(right=50, value=fuel):
            self.fuel_volume = fuel
        else:
            raise TypeError

        if self.checking_in_interval(right=10, value=number):
            self.number_of_parking_days = number
        else:
            raise TypeError

        if self.checking_in_interval(right=10, value=current):
            self.current_parking_day = current
        else:
            raise TypeError

        self.position = self.__ID_LIST[Object.__COUNTER]
        Object.__COUNTER += 1
        # print(self.position)

    @staticmethod
    def checking_in_interval(right, value, left=0):
        return left <= value <= right


class AerialVehicle(Object):
    pass


class GroundVehicle(Object):
    pass


class Aircraft(AerialVehicle):
    pass


class LightSingle_engineAircraft(Aircraft):
    def __init__(self, number: int = 1, current: int = 2, fuel: float = 0):
        super().__init__(number=number, current=current, fuel=fuel)


class TransportAircraft(Aircraft):
    def __init__(self, number: int = 1, current: int = 2, fuel: float = 0, cargo_weight: float = 0):
        super().__init__(number=number, current=current, fuel=fuel)
        if self.checking_in_interval(right=50, value=cargo_weight):
            self.cargo_weight = cargo_weight
        else:
            raise TypeError


class PassengerAircraft(Aircraft):
    def __init__(self, number: int = 1, current: int = 2, fuel: float = 0,
                 number_seats: int = 0, number_passengers: int = 0):
        super().__init__(number=number, current=current, fuel=fuel)

        if self.checking_in_interval(right=50, value=number_seats):
            self.number_seats = number_seats
        else:
            raise TypeError
        if self.checking_in_interval(right=50, value=number_passengers):
            self.number_passengers = number_passengers
        else:
            raise TypeError


class FighterJet(Aircraft):
    def __init__(self, number: int = 1, current: int = 2, fuel: float = 0, number_missiles: int = 0):
        super().__init__(number=number, current=current, fuel=fuel)

        if self.checking_in_interval(right=6, value=number_missiles):
            self.number_missiles = number_missiles
        else:
            raise TypeError


class Helicopter(AerialVehicle):
    pass


class LightHelicopter(Helicopter):
    def __init__(self, number: int = 1, current: int = 2, fuel: float = 0):
        super().__init__(number=number, current=current, fuel=fuel)


class CombatHelicopter(Helicopter):
    def __init__(self, number: int = 1, current: int = 2, fuel: float = 0, number_missiles: int = 0):
        super().__init__(number=number, current=current, fuel=fuel)

        if self.checking_in_interval(right=6, value=number_missiles):
            self.number_missiles = number_missiles
        else:
            raise TypeError


class Bus(GroundVehicle):
    def __init__(self, number: int = 1, current: int = 2, fuel: float = 0,  refueling_status: float = 0):
        super().__init__(number=number, current=current, fuel=fuel)

        if self.checking_in_interval(right=1., value=refueling_status):
            self.number_missiles = refueling_status
        else:
            raise TypeError


class FuelTanker(GroundVehicle):
    pass
