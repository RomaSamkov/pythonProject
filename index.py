# try:
#     with open('data/file.txt', 'r') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('File not found')

import datetime
import sys, os, platform
# from math import sqrt, ceil
import myModule

# print(datetime.datetime.now().time())
# # print(sys.path)
# print(os.name)
# print(platform.system())
# print(ceil(sqrt(25)))

myModule.hello()
print(myModule.name)
myModule.sum_num(1, 2,  3)