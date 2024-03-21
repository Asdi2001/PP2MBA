import json

file = open('sample-data.json', 'r', encoding="utf-8")
data = json.loads(file.read())

interfaces = data['imdata']


print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<5}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)


for interface in interfaces:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')
    print("{:<50} {:<20} {:<10} {:<5}".format(dn, description, speed, mtu))