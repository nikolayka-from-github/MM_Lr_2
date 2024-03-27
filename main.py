import Objects
import random

LIST_NAME_OBJECT = [Objects.Bus, Objects.FuelTanker, Objects.FighterJet,
                    Objects.CombatHelicopter, Objects.LightHelicopter, Objects.PassengerAircraft,
                    Objects.TransportAircraft, Objects.LightSingle_engineAircraft]
LIST_OBJECT = []
for i in range(1, 201):
    pass
    # print(LIST_NAME_OBJECT)
    rand_class = random.randint(0, 7)
    obj = LIST_NAME_OBJECT[rand_class]()
    LIST_OBJECT.append(obj)
    print(obj.get_position)
print(len(LIST_OBJECT))
print(len(LIST_NAME_OBJECT))



