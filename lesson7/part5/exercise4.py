from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

N = 20

pupils = set()
for number in range(N):
    pupils.add("pupil" + str(number))


# set -> list conversion
list_pupils = list(pupils)
math_teams = set()

for i in range(N//2):
    pos1 = randrange(0, len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0, len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1, pupil2)
    math_teams.add(team)
print("math teams: " + str(math_teams))

list_pupils = list(pupils)
geography_teams = set()
for i in range(N//2):
    pos1 = randrange(0, len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0, len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1, pupil2)
    geography_teams.add(team)
print("geaography teams: " + str(geography_teams))