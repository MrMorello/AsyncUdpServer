def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print('display works')


decorated_display = decorator_function(display)

if __name__ == '__main__':
    decorated_display()
