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

def func(h,w):
    return h*w
print(func(2,2))

func_l = lambda h,w: h*w
print(func_l(4,8))