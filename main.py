name = 'Python'
student = "coder"
user_name = input('Write your name:\n')
user_age = int(input('Write your age'))


if user_name == 'Mark' and user_age > 10:
    print('Hello Mark')
    print(f"Your age is {user_age} years")
elif user_name == 'Sponge':
    print('Hello Sponge')
else:
    print(f"Hello {user_name}!")



