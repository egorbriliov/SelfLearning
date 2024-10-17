def repeat(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result: str = func(*args, **kwargs)
                print(result)
        return wrapper
    return decorator

@repeat(3)
def greet(name: str) -> str:
    """Creating greeting stroke with name
    
    Parametrs:
    -------
        name: str
        Name that you would greeted
    
    Rerurn:
    -------
        str:
        greeting stroke with name
    
    """
    return f"Hello, {name}!"

greet("Alex")