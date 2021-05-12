"""In Python 3.9, expressions will be allowed as decorators

See PEP 614: https://www.python.org/dev/peps/pep-0614/
"""
PROD = False


def do_nothing(func):
    return func


def trace(func):
    def _trace(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return _trace


@(do_nothing if PROD else trace)
def greet(name="world"):
    return f"Hello {name}"


greet()