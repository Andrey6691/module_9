import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x==y, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        for x in data_set:
            y = f"{x}\n"
            f = open(file_name, 'a', encoding = 'UTF-8')
            f.write (str(y))
            f.close()

    return write_everything

class MysticBall:

    def __init__ (self, *words):
        self.words = words
    def __call__(self):
        x =  random.choice(self.words)
        return  x



write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Раз', 'Два', 'Три', 'Четыре')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())