animal_weight = []
animal_list = []


class Animal:

    def __init__(self, weight, name):
        self.name = name
        self.weight = weight    #kg

    def feed(self):
        print('Animal fed')


class Milking(Animal):

    def milk(self):
        print('Animal milked')


class Shaving(Animal):

    def shave(self):
        print('Animal shaved')


class EggCollecting(Animal):

    def collect_eggs(self):
        print('Eggs collected')


class Goose(EggCollecting):
    sound = 'honk'
    animal = 'гусь'


goose1 = Goose(7, 'Серый')
animal_weight.append(goose1.weight)
animal_list.append(goose1.animal + ' ' + goose1.name)
goose2 = Goose(8, 'Белый')
animal_weight.append(goose2.weight)
animal_list.append(goose2.animal + ' ' + goose2.name)


class Cow(Milking):
    sound = 'moo'
    animal = 'корова'


cow1 = Cow(500, 'Манька')
animal_weight.append(cow1.weight)
animal_list.append(cow1.animal + ' ' + cow1.name)


class Sheep(Shaving):
    sound = 'baa'
    animal = 'баран'


sheep1 = Sheep(75, 'Барашек')
animal_weight.append(sheep1.weight)
animal_list.append(sheep1.animal + ' ' + sheep1.name)
sheep2 = Sheep(82, 'Кудрявый')
animal_weight.append(sheep2.weight)
animal_list.append(sheep2.animal + ' ' + sheep2.name)


class Chicken(EggCollecting):
    sound = 'cluck'
    animal = 'курица'


chicken1 = Chicken(1.5, 'Ко-Ко')
animal_weight.append(chicken1.weight)
animal_list.append(chicken1.animal + ' ' + chicken1.name)
chicken2 = Chicken(1.3, 'Кукареку')
animal_weight.append(chicken2.weight)
animal_list.append(chicken2.animal + ' ' + chicken2.name)


class Goat(Milking):
    sound = 'bleat'
    animal = 'коза'


goat1 = Goat(53, 'Рога')
animal_weight.append(goat1.weight)
animal_list.append(goat1.animal + ' ' + goat1.name)
goat2 = Goat(61, 'Копыта')
animal_weight.append(goat2.weight)
animal_list.append(goat2.animal + ' ' + goat2.name)


class Duck(EggCollecting):
    sound = 'quack'
    animal = 'утка'


duck1 = Duck(3, 'Кряква')
animal_weight.append(duck1.weight)
animal_list.append(duck1.animal + ' ' + duck1.name)

weight_sum = sum(animal_weight)
max_weight = max(animal_weight)
heaviest_animal_index = animal_weight.index(max_weight)

print('Общий вес всех животных -', weight_sum, 'кг.')
print('Больше всего весит', animal_list[heaviest_animal_index], '-', max_weight, 'кг.')


