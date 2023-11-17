def validator(func):
    def wrapper(w):
        print('Before')
        func(w)
        print('After')
    return wrapper

@validator
def main_func(word):
    print(word)

main_func('Hello!')







