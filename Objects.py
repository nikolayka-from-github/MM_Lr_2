import random


class Object:
    __ID_LIST = list(range(1, 201))
    random.shuffle(__ID_LIST)

    __COUNTER: int = 0

    @staticmethod
    def append_init_file(append_str: str):
        init_f = open("init.txt", 'a')
        init_f.write(append_str + "\n")
        # self.__obj_init_str
        init_f.close()

    def __init__(self, number_of_parking_days: int = 1, current_parking_day: int = 2,
                 fuel_volume: float = 0., position: int = None):
        if self.checking_in_interval(right=50, value=fuel_volume):
            self.fuel_volume = fuel_volume
        else:
            raise TypeError

        if self.checking_in_interval(right=10, value=number_of_parking_days):
            self.number_of_parking_days = number_of_parking_days
        else:
            raise TypeError

        if self.checking_in_interval(right=10, value=current_parking_day):
            self.current_parking_day = current_parking_day
        else:
            raise TypeError
        if position:
            if self.checking_in_interval(right=200, value=position):
                self.position = position
            else:
                raise TypeError
        else:
            self.position = self.__ID_LIST[Object.__COUNTER]
        self._obj_init_str = (f" fuel_volume = {fuel_volume}, number_of_parking_days = {number_of_parking_days},"
                              f" current_parking_day = {current_parking_day}, position = {self.position}")
        # print(self.__obj_init_str)
        Object.__COUNTER += 1
        # print(self.position)

    @staticmethod
    def checking_in_interval(right, value, left=0):
        return left <= value <= right

    @property
    def get_number_of_parking_days(self):
        return self.number_of_parking_days

    @property
    def get_current_parking_day(self):
        return self.current_parking_day

    @property
    def get_position(self):
        return self.position

    @property
    def get_fuel_volume(self):
        return self.fuel_volume


class AerialVehicle(Object):
    ...


class GroundVehicle(Object):
    ...


class Aircraft(AerialVehicle):
    ...


class Helicopter(AerialVehicle):
    ...


class LightSingle_engineAircraft(Aircraft):
    def __init__(self,
                 fuel_volume: float = 0,
                 number_of_parking_days: int = 2,
                 current_parking_day: int = 1,
                 position: int = None,
                 flag_init: bool = False):
        super().__init__(number_of_parking_days=number_of_parking_days,
                         current_parking_day=current_parking_day,
                         fuel_volume=fuel_volume,
                         position=position)
        if flag_init:
            self.append_init_file("LightSingle_engineAircraft:" + self._obj_init_str)


class TransportAircraft(Aircraft):
    def __init__(self,
                 fuel_volume: float = 0.,
                 number_of_parking_days: int = 2,
                 current_parking_day: int = 1,
                 position: int = None,
                 cargo_weight: float = 0.,
                 flag_init: bool = False):
        super().__init__(number_of_parking_days=number_of_parking_days,
                         current_parking_day=current_parking_day,
                         fuel_volume=fuel_volume,
                         position=position)
        if self.checking_in_interval(right=50., value=cargo_weight):
            self.cargo_weight = cargo_weight
        else:
            raise TypeError
        if flag_init:
            self.append_init_file("TransportAircraft:" +
                                  self._obj_init_str +
                                  f", cargo_weight = {cargo_weight}")


class PassengerAircraft(Aircraft):
    def __init__(self,
                 fuel_volume: float = 0.,
                 number_of_parking_days: int = 2,
                 current_parking_day: int = 1,
                 position: int = None,
                 number_seats: int = 0,
                 number_passengers: int = 0,
                 flag_init: bool = False):
        super().__init__(number_of_parking_days=number_of_parking_days,
                         current_parking_day=current_parking_day,
                         fuel_volume=fuel_volume,
                         position=position)
        if self.checking_in_interval(right=50, value=number_seats):
            self.number_seats = number_seats
        else:
            raise TypeError
        if self.checking_in_interval(right=50, value=number_passengers):
            self.number_passengers = number_passengers
        else:
            raise TypeError
        if flag_init:
            self.append_init_file("PassengerAircraft:" +
                                  self._obj_init_str +
                                  f", number_seats = {number_seats}, number_passengers = {number_passengers}")


class FighterJet(Aircraft):
    def __init__(self,
                 fuel_volume: float = 0,
                 number_of_parking_days: int = 2,
                 current_parking_day: int = 1,
                 position: int = None,
                 number_missiles: int = 0,
                 flag_init: bool = False):
        super().__init__(number_of_parking_days=number_of_parking_days,
                         current_parking_day=current_parking_day,
                         fuel_volume=fuel_volume,
                         position=position)
        if self.checking_in_interval(right=6, value=number_missiles):
            self.number_missiles = number_missiles
        else:
            raise TypeError
        #

        if flag_init:
            self.append_init_file("FighterJet:" + self._obj_init_str +
                                  f", number_missiles = {number_missiles}")


class LightHelicopter(Helicopter):
    def __init__(self,
                 fuel_volume: float = 0,
                 number_of_parking_days: int = 2,
                 current_parking_day: int = 1,
                 position: int = None,
                 flag_init: bool = False):
        super().__init__(number_of_parking_days=number_of_parking_days,
                         current_parking_day=current_parking_day,
                         fuel_volume=fuel_volume,
                         position=position)
        if flag_init:
            self.append_init_file("LightHelicopter:" + self._obj_init_str)


class CombatHelicopter(Helicopter):
    def __init__(self,
                 fuel_volume: float = 0,
                 number_of_parking_days: int = 2,
                 current_parking_day: int = 1,
                 position: int = None,
                 number_missiles: int = 0,
                 flag_init: bool = False):
        super().__init__(number_of_parking_days=number_of_parking_days,
                         current_parking_day=current_parking_day,
                         fuel_volume=fuel_volume,
                         position=position)
        if self.checking_in_interval(right=6, value=number_missiles):
            self.number_missiles = number_missiles
        else:
            raise TypeError
        #

        if flag_init:
            self.append_init_file("CombatHelicopter:" + self._obj_init_str +
                                  f", number_missiles = {number_missiles}")


class Bus(GroundVehicle):
    def __init__(self,
                 fuel_volume: float = 0,
                 number_of_parking_days: int = 2,
                 current_parking_day: int = 1,
                 position: int = None,
                 number_seats: int = 0,
                 number_passengers: int = 0,
                 required_position: int = None,
                 flag_init: bool = False):
        super().__init__(number_of_parking_days=number_of_parking_days,
                         current_parking_day=current_parking_day,
                         fuel_volume=fuel_volume,
                         position=position)
        if self.checking_in_interval(right=50, value=number_seats):
            self.number_seats = number_seats
        else:
            raise TypeError
        if self.checking_in_interval(right=50, value=number_passengers):
            self.number_passengers = number_passengers
        else:
            raise TypeError
        if required_position:
            self.required_position = required_position
        else:
            self.required_position = random.randint(1, 201)
        if flag_init:
            self.append_init_file("Bus:" +
                                  self._obj_init_str +
                                  f", number_seats = {number_seats}, "
                                  f" number_passengers = {number_passengers},"
                                  f" required_position = {self.required_position}")


class FuelTanker(GroundVehicle):
    def __init__(self,
                 fuel_volume: float = 0,
                 number_of_parking_days: int = 2,
                 current_parking_day: int = 1,
                 position: int = None,
                 refueling_status: float = 0,
                 required_position: int = None,
                 flag_init: bool = False):
        super().__init__(number_of_parking_days=number_of_parking_days,
                         current_parking_day=current_parking_day,
                         fuel_volume=fuel_volume,
                         position=position)

        if required_position:
            self.required_position = required_position
        else:
            self.required_position = random.randint(1, 201)

        if self.checking_in_interval(right=1., value=refueling_status):
            self.refueling_status = refueling_status

        if flag_init:
            self.append_init_file("FuelTanker:" +
                                  self._obj_init_str +
                                  f", refueling_status = {self.refueling_status}"
                                  f", required_position = {self.required_position}")