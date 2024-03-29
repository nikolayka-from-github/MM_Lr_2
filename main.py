import Objects
import AirportDocker
import random

LIST_NAME_OBJECT = [Objects.LightSingle_engineAircraft, Objects.TransportAircraft, Objects.PassengerAircraft,
                    Objects.LightHelicopter, Objects.CombatHelicopter, Objects.FighterJet,
                    Objects.FuelTanker, Objects.Bus]


def generate_init_file():
    for i in range(1, 201):
        rand_class = random.randint(0, 7)
        number_of_parking_days = random.randint(0, 10)
        current_parking_day = random.randint(0, 10)
        fuel_volume = random.uniform(0, 50)
        # position = position
        if rand_class == 0:
            LIST_NAME_OBJECT[rand_class](
                number_of_parking_days=number_of_parking_days,
                current_parking_day=current_parking_day,
                fuel_volume=fuel_volume,
                flag_init=True)
        if rand_class == 1:
            cargo_weight = random.uniform(0, 50)
            LIST_NAME_OBJECT[rand_class](
                number_of_parking_days=number_of_parking_days,
                current_parking_day=current_parking_day,
                fuel_volume=fuel_volume,
                cargo_weight=cargo_weight,
                flag_init=True)
        if rand_class == 2:
            number_seats = random.randint(0, 50)
            number_passengers = random.randint(0, 50)
            LIST_NAME_OBJECT[rand_class](
                number_of_parking_days=number_of_parking_days,
                current_parking_day=current_parking_day,
                fuel_volume=fuel_volume,
                number_seats=number_seats,
                number_passengers=number_passengers,
                flag_init=True)
        if rand_class == 3:
            LIST_NAME_OBJECT[rand_class](
                number_of_parking_days=number_of_parking_days,
                current_parking_day=current_parking_day,
                fuel_volume=fuel_volume,
                flag_init=True)
        if rand_class == 4 or rand_class == 5:
            number_missiles = random.randint(0, 6)
            LIST_NAME_OBJECT[rand_class](
                number_of_parking_days=number_of_parking_days,
                current_parking_day=current_parking_day,
                fuel_volume=fuel_volume,
                number_missiles=number_missiles,
                flag_init=True)
        if rand_class == 6:
            refueling_status = random.uniform(0., 1.)
            required_position = random.randint(1, 201)
            LIST_NAME_OBJECT[rand_class](
                number_of_parking_days=number_of_parking_days,
                current_parking_day=current_parking_day,
                fuel_volume=fuel_volume,
                refueling_status=refueling_status,
                required_position=required_position,
                flag_init=True)
        if rand_class == 7:
            number_seats = random.randint(0, 50)
            number_passengers = random.randint(0, 50)
            required_position = random.randint(1, 201)
            LIST_NAME_OBJECT[rand_class](
                number_of_parking_days=number_of_parking_days,
                current_parking_day=current_parking_day,
                fuel_volume=fuel_volume,
                number_seats=number_seats,
                number_passengers=number_passengers,
                required_position=required_position,
                flag_init=True)


AA = AirportDocker.AirportDocker("init.txt")
print("len: ", len(AA.list_PassengerAircraft))
for i in AA:
    obj = i
    print(obj.get_position)

