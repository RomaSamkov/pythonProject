class Robot:
    name = None
    age = None
    isAI = None

    def set_data(self, robo_name, robo_age, robo_isAI):
        self.name = robo_name
        self.age = robo_age
        self.isAI = robo_isAI

    def get_data(self):
        print(f'{self.name} age: {self.age} and AI: {self.isAI}')


robot1 = Robot()
robot1.set_data('Kevin' ,13, True)
robot2 = Robot()
robot2.name = 'Bob'
robot2.age = 22
robot2.isAI = False

robot1.get_data()
robot2.get_data()