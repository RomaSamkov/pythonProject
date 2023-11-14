# try:
#     with open('data/file.txt', 'r') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('File not found')

import datetime
import sys, os, platform

print(datetime.datetime.now().time())
# print(sys.path)
print(os.name)
print(platform.system())