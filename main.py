fruits = ['banana', 'orange', 'apple', 'coconut']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(1, 10, 2)))
print(fruits[0:3])
print(f'{numbers=}')
print(f'{fruits=}')


def intro(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)


intro(name="John", age=30, city='New York')