import os

# directory to m9k addon folder
weaponsdir = ""

rifle = "M9K Assault Rifles"
sniper = "M9K Sniper Rifles"
pistol = "M9K Pistols"

top = {
    "name": "",
    "damage": 0,
    "spread": 69.69,
    "rpm": 0,
    "category": "not set"
}
second = {
    "name": "",
    "damage": 0,
    "spread": 69.69,
    "rpm": 0,
    "category": "not set"
}
third = {
    "name": "",
    "damage": 0,
    "spread": 69.69,
    "rpm": 0,
    "category": "not set"
}
weapons = { }

# get guns and values we need
for path, subdirs, files in os.walk(weaponsdir):
    if files:
        for file in files:
            damage = 0
            spread = 0.1
            rpm = 0
            category = ""
            f = open(os.path.join(path, file))
            lines = f.readlines()
            try:
                for line in lines:
                    if "SWEP.Primary.Damage" in line:
                        damage = int(line.split('=')[1].strip(' ').split('-', 1)[0].split('\t', 1)[0])
                    if "SWEP.Primary.Spread" in line:
                        spread = float(line.split('=')[1].strip(' ').split('-', 1)[0].split('\t', 1)[0])
                    if "SWEP.Primary.RPM" in line:
                        rpm = int(line.split('=')[1].strip(' ').split('-', 1)[0].split('\t', 1)[0])
                    if "SWEP.Category" in line:
                        category = str(line.split('=')[1].strip(' ').strip('"').split('-', 1)[0].split('\t', 1)[:-2])
                weapons[path] = {
                    "name": path,
                    "damage": damage,
                    "spread": spread,
                    "rpm": rpm,
                    "category": category
                }
            except UnicodeDecodeError:
                continue
            f.close()

# sort and find out the best 3 guns based off damage and spread
# for i in range(3):
#     for gun in weapons:
#         print(weapons[gun]["category"])
#         if i == 0 and weapons[gun]["category"] == rifle:
#             if weapons[gun]["damage"] > top["damage"] and weapons[gun]["spread"] < top["spread"] and weapons[gun]["rpm"] > top["rpm"]:
#                 top = {
#                     "name": str(gun),
#                     "damage": weapons[gun]["damage"],
#                     "spread": weapons[gun]["spread"],
#                     "rpm": weapons[gun]["rpm"],
#                     "category": weapons[gun]["category"]
#                 }

#         if i == 1 and gun != top["name"] and weapons[gun]["category"] == sniper:
#             if weapons[gun]["damage"] > second["damage"] and weapons[gun]["spread"] < second["spread"] and weapons[gun]["rpm"] > second["rpm"]:
#                 second = {
#                     "name": str(gun),
#                     "damage": weapons[gun]["damage"],
#                     "spread": weapons[gun]["spread"],
#                     "rpm": weapons[gun]["rpm"],
#                     "category": weapons[gun]["category"]
#                 }

#         if i == 2 and gun != top["name"] and gun != second["name"] and weapons[gun]["category"] == pistol:
#             if weapons[gun]["damage"] > third["damage"] and weapons[gun]["spread"] < third["spread"] and weapons[gun]["rpm"] > third["rpm"]:
#                 third = {
#                     "name": str(gun),
#                     "damage": weapons[gun]["damage"],
#                     "spread": weapons[gun]["spread"],
#                     "rpm": weapons[gun]["rpm"],
#                     "category": weapons[gun]["category"]
#                 }

for i in range(3):
    for gun in weapons:
        if i == 0:
            if weapons[gun]["damage"] > top["damage"] and weapons[gun]["spread"] < top["spread"] and weapons[gun]["rpm"] > top["rpm"]:
                top = {
                    "name": str(gun),
                    "damage": weapons[gun]["damage"],
                    "spread": weapons[gun]["spread"],
                    "rpm": weapons[gun]["rpm"]
                }

        if i == 1 and gun != top["name"]:
            if weapons[gun]["damage"] > second["damage"] and weapons[gun]["spread"] < second["spread"] and weapons[gun]["rpm"] > second["rpm"]:
                second = {
                    "name": str(gun),
                    "damage": weapons[gun]["damage"],
                    "spread": weapons[gun]["spread"],
                    "rpm": weapons[gun]["rpm"]
                }

        if i == 2 and gun != top["name"] and gun != second["name"]:
            if weapons[gun]["damage"] > third["damage"] and weapons[gun]["spread"] < third["spread"] and weapons[gun]["rpm"] > third["rpm"]:
                third = {
                    "name": str(gun),
                    "damage": weapons[gun]["damage"],
                    "spread": weapons[gun]["spread"],
                    "rpm": weapons[gun]["rpm"]
                }


print(top)
print(second)
print(third)