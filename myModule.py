name = 'Kevin'


def hello():
    print('Hello!')


def sum_num(a, b, c):
    print(a+b+c)


class Car:
    name = 'Drive'
    def get_drive(self):
        print(f'Hello {name} your car name is {self.name} !')

car = Car()
car.get_drive()

print('''Text row
and another text row''')

s = 'Hello, nice to meet you, \n your name is %s and your job is %s '
print(s %('Kevin','Developer'))