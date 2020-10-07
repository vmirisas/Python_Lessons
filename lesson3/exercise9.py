hours = int(input("type hours: "))
minutes = int(input("type minutes: "))
seconds = int(input("type seconds: "))


if hours < 10:
    str_hours = "0" + str(hours)
else:
    str_hours = str(hours)

if minutes < 10:
    str_minutes = "0" + str(minutes)
else:
    str_minutes = str(minutes)

if seconds < 10:
    str_seconds = "0" + str(seconds)
else:
    str_seconds = str(seconds)


print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
print(str_hours + ":" + str_minutes + ":" + str_seconds)