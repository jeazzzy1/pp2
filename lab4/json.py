import json

with open('sample-data.json') as diction:
    data = json.load(diction)
    
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

for s in data["imdata"]:
    print(s['l1PhysIf']['attributes']['dn'],'         ',s['l1PhysIf']['attributes']['descr'],'                  ',s['l1PhysIf']['attributes']['speed'],' ',s['l1PhysIf']['attributes']['mtu'])


    