def my_decorator_function(func):
    def wrapper_function():
        print('start ....')
        func()
        print('End .....')
    return wrapper_function


@my_decorator_function
def hello():
    print('hello world ...')
        
hello()