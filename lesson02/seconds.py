time_in_seconds = 10000

hours = time_in_seconds // 3600
print("hours:", hours)

seconds = time_in_seconds % 3600
minutes = seconds // 60
print("minutes:", minutes)

seconds = seconds % 60
print("seconds:", seconds)

print(time_in_seconds, "seconds equals to", hours, "hours", minutes, "minutes and", seconds, "seconds")
print(time_in_seconds, "seconds =", hours, ":", minutes, ":", seconds)
