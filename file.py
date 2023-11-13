file = open('data/file.txt', 'a')
data = input('Write your hobby: \n')
file.write(f'Your hobby is {data}')

file.close()