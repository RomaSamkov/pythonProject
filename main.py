name = 'Python'
student = "coder"
# user_name = input('Write your name:\n')
# user_age = int(input('Write your age'))


# if user_name == 'Mark' and user_age > 10:
#     print('Hello Mark')
#     print(f"Your age is {user_age} years")
# elif user_name == 'Sponge':
#     print('Hello Sponge')
# else:
#     print(f"Hello {user_name}!")


cost = 110

if cost > 100:
    cost = cost - cost * 0.03
elif cost > 500:
    cost = cost - cost * 0.05
if cost > 1000:
    cost = cost - cost * 0.1
print(cost)