class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        sec = self.__second + other.__second
        extra_min = sec // 60
        sec = sec % 60

        mins = self.__minute + other.__minute + extra_min
        extra_hour = mins // 60
        mins = mins % 60

        hrs = self.__hour + other.__hour + extra_hour
        hrs = hrs % 24

        return Time(hrs, mins, sec)

    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")


t1 = Time(2, 45, 50)
t2 = Time(3, 20, 30)

t3 = t1 + t2

t1.display()
t2.display()
t3.display()