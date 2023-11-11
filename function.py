# def sum_sum(*any_numbers):
#     for num in any_numbers:
#         print(num)
#
# sum_sum(1,2,3,4,5,6)

# def func_max(num_list):
#     max = 0
#     for i in num_list:
#         if i > max:
#             max = i
#     return max
#
# r = func_max([1,2,3,4,5,6,7,11])
# print(r)

# def func_char(string):
#     return len(string)
#
# result = func_char('JavaScript and Python')
# print(result)

# def func_pow(n,pow):
#     if pow > 0 and n  > 0:
#         return n**pow
#     return 'not minus'
#
# print(func_pow(2,2))

# l = lambda x,y : x**y
#
# print(l(2,8))

# def foo(n):
#     if n >= 1:
#         foo(n-1)
#         print(n)
# foo(88)

# def func(h,w):
#     return h*w
# print(func(2,2))
#
# func_l = lambda h,w: h*w
# print(func_l(4,8))

# def func_divide(n, d):
#     try:
#         r = n / d
#     except:
#         return 'Dont divide to zero'
#
#     return r
#
#
# print(func_divide(1, 0))

# def name_month(n):
#     try:
#         month_index = n - 1
#         m = []
#         import calendar
#         for month in calendar.month_name:
#             m.append(month)
#
#         m.pop(0) #remove the empty value
#         return m[month_index]
#     except TypeError:
#         return  'Write integer'
#     except IndexError:
#         return  "Write month in 1 and 12"
#
# print(name_month(12))

# def func(l):
#     try:
#         return  len(l[:]) == len(set(l))
#     except TypeError:
#         return 'Only type'

# print(func([1, 2, 3, 4, 6]))
print(func({}))



