import os

def some_function():
    current_mode = os.getenv('ENVIRONMENT')
    print(f'This is a : {current_mode}')

