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


# cost = int(input('Fill your sum \n'))
# if cost > 1000:
#     cost = cost - cost * 0.1
# elif cost > 500:
#     cost = cost - cost * 0.05
# elif cost > 100:
#     cost = cost - cost * 0.03
#
#
# print(cost)

# line = input('Write the string: \n')
#
# # if bool(line):
# #     print(line)
# # else:
# #     print(None)
#
# print(line if line else None)

# for i in range(100):
#     if i != 0 and i % 2 == 0:
#         print(i)
#
# for word in 'hello':
#     r = 'hello'.replace('l','s')
#     print(r)

# for el in reversed(range(105)):
#     if el % 5 == 0:
#         print(el)
#         break

sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum2 = [4, 2, 3, 1, 5, 6, 11, 8, 9, 7, 10]
# sum.append('item')
# sum.extend(sum2)
# el = sum.pop(6)
# print(el)
# sum.reverse()
# sum2.sort()
# # sum2.sort(reverse=True)
# print(sum)
# print(sum2)

for num in sum:
    if num % 2 == 0:
        sum.remove(num)
print(sum)