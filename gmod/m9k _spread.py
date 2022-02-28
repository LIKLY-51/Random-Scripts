import os

# directory to m9k addon folder
weaponsdir = ""

top = {
    "name": "",
    "damage": 0,
    "spread": 69.69,
    "rpm": 0
}
second = {
    "name": "",
    "damage": 0,
    "spread": 69.69,
    "rpm": 0
}
third = {
    "name": "",
    "damage": 0,
    "spread": 69.69,
    "rpm": 0
}
weapons = { }

# get guns and values we need
for path, subdirs, files in os.walk(weaponsdir):
    if files:
        for file in files:
            damage = 0
            spread = 0.1
            rpm = 0
            f = open(os.path.join(path, file))
            lines = f.readlines()
            try:
                for line in lines:
                    if "SWEP.Primary.Damage" in line:
                        damage = int(line.split('=')[1].strip(' '))
                    if "SWEP.Primary.Spread" in line:
                        spread = float(line.split('=')[1].strip(' '))
                    if "SWEP.Primary.RPM" in line:
                        rpm = int(line.split('=')[1].strip(' '))
                weapons[path] = {
                    "name": path,
                    "damage": damage,
                    "spread": spread,
                    "rpm": rpm
                }
            except UnicodeDecodeError:
                continue
            f.close()

# sort and find out the best 3 guns based off damage and spread
for i in range(3):
    for gun in weapons:
        if i == 0:
            if weapons[gun]["spread"] < top["spread"]:
                top = {
                    "name": str(gun),
                    "damage": weapons[gun]["damage"],
                    "spread": weapons[gun]["spread"],
                    "rpm": weapons[gun]["rpm"]
                }

        if i == 1 and gun != top["name"]:
            if weapons[gun]["spread"] < second["spread"]:
                second = {
                    "name": str(gun),
                    "damage": weapons[gun]["damage"],
                    "spread": weapons[gun]["spread"],
                    "rpm": weapons[gun]["rpm"]
                }

        if i == 2 and gun != top["name"] and gun != second["name"]:
            if weapons[gun]["spread"] < third["spread"]:
                third = {
                    "name": str(gun),
                    "damage": weapons[gun]["damage"],
                    "spread": weapons[gun]["spread"],
                    "rpm": weapons[gun]["rpm"]
                }


print(top)
print(second)
print(third)