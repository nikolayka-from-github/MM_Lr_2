import Objects

LIST_NAME_OBJECT = [Objects.LightSingle_engineAircraft, Objects.TransportAircraft, Objects.PassengerAircraft,
                    Objects.LightHelicopter, Objects.CombatHelicopter, Objects.FighterJet,
                    Objects.FuelTanker, Objects.Bus]


class AirportDocker:
    list_LightSingle_engineAircraft = []
    list_TransportAircraft = []
    list_PassengerAircraft = []
    list_LightHelicopter = []
    list_CombatHelicopter = []
    list_FighterJet = []
    list_FuelTanker = []
    list_Bus = []

    def __init__(self, init_file: str):
        with open(init_file, "r") as file1:
            for line in file1:
                line = line.split(":")
                line_ = line[1].split(",")
                for j in range(0, len(line_)):
                    line_[j] = line_[j].split()
                if line[0] == "LightSingle_engineAircraft":
                    obj = Objects.LightSingle_engineAircraft(
                        number_of_parking_days=int(line_[1][2]),
                        current_parking_day=int(line_[2][2]),
                        fuel_volume=float(line_[0][2]),
                        position=int(line_[3][2]),
                        flag_init=False)
                    self.list_LightSingle_engineAircraft.append(obj)

                if line[0] == "TransportAircraft":
                    obj = Objects.TransportAircraft(
                        number_of_parking_days=int(line_[1][2]),
                        current_parking_day=int(line_[2][2]),
                        fuel_volume=float(line_[0][2]),
                        position=int(line_[3][2]),
                        cargo_weight=float(line_[4][2]),
                        flag_init=False)
                    self.list_TransportAircraft.append(obj)
                if line[0] == "PassengerAircraft":
                    obj = Objects.PassengerAircraft(
                        number_of_parking_days=int(line_[1][2]),
                        current_parking_day=int(line_[2][2]),
                        fuel_volume=float(line_[0][2]),
                        position=int(line_[3][2]),
                        number_seats=int(line_[4][2]),
                        number_passengers=int(line_[5][2]),
                        flag_init=False)
                    self.list_PassengerAircraft.append(obj)
                if line[0] == "LightHelicopter":
                    obj = Objects.LightHelicopter(
                        number_of_parking_days=int(line_[1][2]),
                        current_parking_day=int(line_[2][2]),
                        fuel_volume=float(line_[0][2]),
                        position=int(line_[3][2]),
                        flag_init=False)
                    self.list_LightHelicopter.append(obj)
                if line[0] == "CombatHelicopter":
                    obj = Objects.CombatHelicopter(
                        number_of_parking_days=int(line_[1][2]),
                        current_parking_day=int(line_[2][2]),
                        fuel_volume=float(line_[0][2]),
                        position=int(line_[3][2]),
                        number_missiles=int(line_[4][2]),
                        flag_init=False)
                    self.list_CombatHelicopter.append(obj)
                if line[0] == "FighterJet":
                    obj = Objects.FighterJet(
                        number_of_parking_days=int(line_[1][2]),
                        current_parking_day=int(line_[2][2]),
                        fuel_volume=float(line_[0][2]),
                        position=int(line_[3][2]),
                        number_missiles=int(line_[4][2]),
                        flag_init=False)
                    self.list_FighterJet.append(obj)
                if line[0] == "FuelTanker":
                    obj = Objects.FuelTanker(
                        number_of_parking_days=int(line_[1][2]),
                        current_parking_day=int(line_[2][2]),
                        fuel_volume=float(line_[0][2]),
                        position=int(line_[3][2]),
                        refueling_status=float(line_[4][2]),
                        required_position=int(line_[5][2]),
                        # number_missiles=int(line_[4][2]),
                        flag_init=False)
                    self.list_FuelTanker.append(obj)
                if line[0] == "Bus":
                    obj = Objects.Bus(
                        number_of_parking_days=int(line_[1][2]),
                        current_parking_day=int(line_[2][2]),
                        fuel_volume=float(line_[0][2]),
                        position=int(line_[3][2]),
                        number_seats=int(line_[4][2]),
                        number_passengers=int(line_[5][2]),
                        required_position=int(line_[6][2]),
                        flag_init=False)
                    self.list_Bus.append(obj)
                # print(self.list_PassengerAircraft[0].get_position())
