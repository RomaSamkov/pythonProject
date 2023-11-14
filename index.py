try:
    with open('data/file.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')