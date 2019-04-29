class Animal:

    def __init__(self, weight, name):
        self.name = name
        self.weight = weight    #kg

    def feed(self):
        print('Животное накормлено')


class Milking(Animal):

    def milk(self):
        print('Животное подоено')


class Shaving(Animal):

    def shave(self):
        print('Животное пострижено')


class EggCollecting(Animal):

    def collect_eggs(self):
        print('Яйца собраны')


class Goose(EggCollecting):
    sound = 'honk'


goose1 = Goose(7, 'Серый')
goose2 = Goose(8, 'Белый')


class Cow(Milking):
    sound = 'moo'


cow1 = Cow(500, 'Манька')


class Sheep(Shaving):
    sound = 'baa'


sheep1 = Sheep(75, 'Барашек')
sheep2 = Sheep(82, 'Кудрявый')


class Chicken(EggCollecting):
    sound = 'cluck'


chicken1 = Chicken(1.5, 'Ко-Ко')
chicken2 = Chicken(1.3, 'Кукареку')


class Goat(Milking):
    sound = 'bleat'


goat1 = Goat(53, 'Рога')
goat2 = Goat(61, 'Копыта')


class Duck(EggCollecting):
    sound = 'quack'


duck1 = Duck(3, 'Кряква')

