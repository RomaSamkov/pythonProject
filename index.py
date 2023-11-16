class Robot:
    name = None
    age = None
    isAI = None

    def __init__(self, robo_name, robo_age, robo_is_ai):
        self.set_data(robo_name, robo_age, robo_is_ai)
        self.get_data()

    def set_data(self, robo_name, robo_age, robo_is_ai):
        self.name = robo_name
        self.age = robo_age
        self.isAI = robo_is_ai

    def get_data(self):
        print(f'{self.name} age: {self.age} and AI: {self.isAI}')


robot1 = Robot('Kevin' ,13, True)
# robot1.set_data('Kevin' ,13, True)
robot2 = Robot('Bob', 22, False)
# robot2.name = 'Bob'
# robot2.age = 22
# robot2.isAI = False

# robot1.get_data()
# robot2.get_data()