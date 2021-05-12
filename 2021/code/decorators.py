import functools


# Introduction
def greet(name, printer=print):
    printer(f"Hi {name}!")


def tnirp(text):
    print(text[::-1])


def prefix_factory(prefix):
    def prefix_printer(text):
        print(f"{prefix}: {text}")

    return prefix_printer


def reverse_factory(func):
    def reverse_caller(text):
        func(text[::-1])

    return reverse_caller


# Excercise 1
def before_and_after_1(func):
    def wrapper(text):
        print("BEFORE")
        func(text)
        print("AFTER")

    return wrapper


def params(*args, **kwargs):
    print(f"{args = }")
    print(f"{kwargs = }")


def before_and_after(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        value = func(*args, **kwargs)
        print("AFTER")
        return value

    return wrapper


# Exercise 2
def do_twice_1(func):
    def wrapper(*args, **kwargs):
        first = func(*args, **kwargs)
        second = func(*args, **kwargs)
        return first, second

    return wrapper


def define(func):
    print(f"Defining {func.__name__}")
    return func


# Exercise 3
FUNCTIONS = {}


def register(func):
    FUNCTIONS[func.__name__] = func
    return func


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        first = func(*args, **kwargs)
        second = func(*args, **kwargs)
        return first, second

    return wrapper


# Exercise 4
def retry_1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Retrying ({e})")

    return wrapper


@retry_1
def process_file(path):
    print(path.read_text())


# Exercise 5
def retry_2(exception):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    print(f"Retrying ({e})")

        return wrapper

    return decorator


# Exercise 6
def retry_3(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying ({e})")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_4(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries - wrapper.num_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying ({e})")
                    wrapper.num_retries += 1
            return func(*args, **kwargs)

        wrapper.num_retries = 0
        return wrapper

    return decorator


class BeforeAndAfter:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print("BEFORE")
        value = self.func(*args, **kwargs)
        print("AFTER")
        return value


# Exercise 7
class Retry:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_retries = 0

    def __call__(self, *args, **kwargs):
        while True:
            try:
                return self.func(*args, **kwargs)
            except Exception:
                self.num_retries += 1
                print(f"Retry attempt {self.num_retries}")
