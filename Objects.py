class Object:
    def __init__(self, start: int = None, current: int = None, fuel: float = 0):
        if self.checking_in_interval(right=50, value=fuel):
            self.fuel_volume = fuel
        else:
            raise TypeError

        if self.checking_in_interval(right=10, value=start):
            self.number_of_parking_days = start
        else:
            raise TypeError

        if self.checking_in_interval(right=10, value=current):
            self.current_parking_day = current
        else:
            raise TypeError

    @staticmethod
    def checking_in_interval(right: int, value, left: int = 0):
        return left <= value <= right


class AerialVehicle(Object):
    def __init__(self):
        super().__init__()


class GroundVehicle(Object):
    def __init__(self):
        super().__init__()


class Aircraft(AerialVehicle):
    pass


class LightSingle_engineAircraft(Aircraft):
    pass


class TransportAircraft(Aircraft):
    pass


class PassengerAircraft(Aircraft):
    pass


class FighterJet(Aircraft):
    pass


class Helicopter(AerialVehicle):
    pass


class LightHelicopter(Helicopter):
    pass


class CombatHelicopter(Helicopter):
    pass


class Bus(GroundVehicle):
    pass


class FuelTanker(GroundVehicle):
    pass

# class LightSingle_engineAircraft(Aircraft):
#     def __init__(self):
#         super().__init__()
#
# class TransportAircraft(Aircraft):
#     def __init__(self):
#         super().__init__()
#
#
# class PassengerAircraft(Aircraft):
#     def __init__(self):
#         super().__init__()
#
#
# class FighterJet(Aircraft):
#     def __init__(self):
#         super().__init__()
# Aircraft
# Transport aircraft
# Passenger aircraft
# Fighter jet
#
# Light helicopter
# Combat helicopter
#
# Ground transportation
#
# Fuel tanker
# Bus
