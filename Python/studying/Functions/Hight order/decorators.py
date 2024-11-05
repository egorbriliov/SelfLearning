from datetime import datetime

# Decorator with using *args and **kwargs
def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@decorator
def example(stroke: str, times: int = 1):
    for _ in range(times):
        print(stroke)

# example("args + kwargs", times=2)


# Decorator with parameters for decorator
def repeat(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result: str = func(*args, **kwargs)
                print(result)
        return wrapper
    return decorator

@repeat(times=3)
def greet(name: str) -> str:
    """Creating greeting stroke with name
    
    Parameters:
    -------
        name: str
        Name that you would greet
    
    Return:
    -------
        str:
        greeting stroke with name
    
    """
    return f"Hello, {name}!"

# greet("Alex")

