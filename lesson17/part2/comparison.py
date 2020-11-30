class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:" \
               f"{str(self.minute).zfill(2)}:" \
               f"{str(self.second).zfill(2)}"

    def __gt__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True
            elif self.minute == other.minute:
                if self.second > other.second:
                    return True
        return False

    def __ge__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True
            elif self.minute == other.minute:
                if self.second >= other.second:
                    return True
        return False

    def __eq__(self, other):
        if isinstance(other, Time):
            if self.hour == other.hour and self.minute == other.minute and self.second == other.second:
                return True
            return False
        elif isinstance(other, int):
            return self == Time(other, 0, 0)


t = Time(11, 2, 3)
t2 = Time(11, 11, 1)
print(f"{t} > {t2}: {t > t2}")
print(f"{t} < {t2}: {t < t2}")
print(f"{t} >= {t2}: {t >= t2}")
print(f"{t} <= {t2}: {t <= t2}")
print(f"{t} == {t2}: {t == t2}")
print(f"{t} != {t2}: {t != t2}")

t = Time(2,0,0)
print(f"{t} == {2}: {t == 2}")
print(f"{2} == {t}: {2 == t}")