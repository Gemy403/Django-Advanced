import time

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'excution time for {func.__name__} = {end_time - start_time}')
    return wrapper


@calculate_execution_time
def my_function():
    for x in range (1000000000):
        pass

my_function()