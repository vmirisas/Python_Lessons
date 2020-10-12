heroes_weapons = {
    "Black Panther": "Anti-Metal Claws",
    "Wolverine": "Claws",
    "Ultron": "Plasma Weapons",
    "Spider-Man": "Web-shooters",
    "Beast": "Claws",
    "Venom": "Web-shooters"
}

print("Key-value loop: ")
for key, value in heroes_weapons.items():
    print(key + " has " + value)

print("\nOrdered key loop: ")
for key in sorted(heroes_weapons.keys()):
    print(key + " has " + heroes_weapons[key])

print("\nReverse Ordered key loop: ")
for key in sorted(heroes_weapons.keys(), reverse=True):
    print(key + " has " + heroes_weapons[key])

print("\nWeapon Gallery: ")
for value in set(heroes_weapons.values()):
    print(value, end=", ")
