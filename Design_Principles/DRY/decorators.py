"""
    using decorators for cross-cutting concerns

    Suppose we need to write logging for multiple functions.

    we can write a common function for this and use it in
    multiple functions.

"""

def logger(fun):
    def wrapper(*args, **kwargs):
        print(f"called function {fun.__name__} with args : {args} & kwargs : {kwargs}")
        return fun(*args, **kwargs)
    return wrapper


@logger
def add(a, b, **kwargs):
    print(f"kwargs are {kwargs}")
    return a+b

@logger
def multiply(a, b, **kwargs):
    print(f"kwargs are {kwargs}")
    return a*b

add_result = add(2, 3, c = {1:2}, d = "name")
multipy_result = multiply(5, 6, c={1:2}, d=[1,2])