bffs = ["Kostas", "Mitsos", "Manos"]
party_guests = ["Anna", "Makis", "Harry", "Tonia", "Elias", "Kostas", "Mitsos", "Sakis", "irene", "Eleni"]
counter = 0
for friend in bffs:
    for person in party_guests:
        print(friend + " " + person)
        if friend == person:
            counter += 1
    print(counter)
    print()


if counter >= 2:
    print("invitation accepted")
else:
    print("invitation denied")