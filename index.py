class Car:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city
        # self.get_info()

    def get_info(self):
        print(f'Car is age: {self.year} and production in: {self.city}', sep='')


class Cooper(Car):
    pass


class Auto(Car):
    wheels = None
    def __init__(self, year, city, wheels):
        super(Auto, self).__init__(year, city)
        self.wheels = wheels

    def get_info(self):
        print(f'wheels: {self.wheels}')
        super().get_info()


cooper = Cooper(12, 'LA')
cooper.get_info()
auto = Auto(8, 'NewYork',8)
auto.get_info()
