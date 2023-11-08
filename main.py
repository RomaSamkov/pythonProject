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

# for num in sum:
#     if num % 2 == 0:
#         sum.remove(num)
# print(sum)

# list_square = []
# for num in sum:
#     list_square.append(num**2)
# print(list_square)
# print('*' * 30)
#
# for i in range(len(sum)):
#     sum[i] = sum[i] ** 2
# print(sum)

# maximum = sum2[0]
# for i in range(len(sum2)):
#     if sum2[i] > maximum:
#         maximum = sum2[i]
# print(maximum)
# # V2
# print(max(sum2))
# # V3
# print(sorted(sum2)[-1])
# # V4
# sum2.sort()
# print(sum2[-1])


obj = {'key': 'value','key2': 'value2'}
# print(obj['key'])
# print(obj)

# for k , v in obj.items():
#     print(f'{k} and {v}')

# print(obj.pop('key'))
# print(obj.values())
# print(obj.keys())

# some_list = ['JavaScript', 'Python', 'SQL', 'React','JavaScript', 'Python']
#
# answer = {}
#
# for e in some_list:
#     if e in answer.keys():
#         answer[e] += 1
#     else:
#         answer[e] = 1
# print(answer)
#
# # V2
#
# for e in some_list:
#     answer[e] = some_list.count(e)
# print(answer)

some_dict = {11:'JavaScript', 'string':'Python', 33:'SQL', 'some string':'React', 5:'JavaScript', 88:'Python'}

# for k, val in some_dict.items():
#     if k % 2 == 0:
#         print(val)
#
# dictionary = {}.fromkeys(range(10), "Any value")
# print('D: ', dictionary)
# some_dict_copy = some_dict.copy()
# for k in some_dict:
#     if type(k) == str:
#         del some_dict_copy[k]
# print(some_dict_copy)

