from time import time
def performance(fn):
    def function(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'{t2-t1} seconds')
        return result
    return function


while True:
    calculator = input(
        'What operation would you like to preform? press "m" for multiply, "d" for devide or "e" to exit: ')
    if calculator == 'm':
        @performance
        def multiply():
            m = int(input('Enter a number to calculate time, multiply by 5: '))
            for x in range(m):
                x = m*5
            print(x)

        multiply()
    elif calculator == 'd':
        @performance
        def devide():
            d = int(input('Enter a number to calculate time, devide by 5: '))
            for x in range(d):
                x = d/5
            print(x)
        devide()
    else:
        print('Thank you. Bue!!!')
        break;
