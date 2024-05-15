def my_decorator_function(func):
    def wrapper_function():
        result = func()
        return result.upper()
    return wrapper_function

@my_decorator_function
def hello():
    return 'hello world ..'
        
print(hello())