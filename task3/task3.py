class BaseConverter:

    def __init__(self, celsius):
        self.celsius = celsius

    def convert(self, type):
        if type:
            return self.celsius * 9/5 + 32
        else:
            return self.celsius + 273 

test = BaseConverter(int(input('Введите температуру: ')))
type = int(input('Первод в Кельвины или Фаренгейты (введите 0 или 1): '))
print (test.convert(type))