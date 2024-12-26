class WatchCalc:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def angleCalc(self):
        firstSide  = self.hours * 30
        secondSide = self.minutes * 6
        angle = abs(firstSide - secondSide)
        if angle > 180:
            return angle % 180
        else:
            return angle

time = input('Введите часы и минуты через пробел: ').split(' ')
test = WatchCalc(int(time[0]), int(time[1]))
print(test.angleCalc())