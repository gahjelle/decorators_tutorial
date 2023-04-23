import functools
import time


#
# Introduction
#
def prefix_factory(prefix):
    def prefix_printer(text):
        print(f"{prefix}: {text}")

    return prefix_printer


def reverse_factory(func):
    def reverse_caller(text):
        func(text[::-1])

    return reverse_caller


#
# Exercise 1
#
def before_and_after_1(func):
    def wrapper(text):
        print("BEFORE")
        func(text)
        print("AFTER")

    return wrapper


def before_and_after_2(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        func(*args, **kwargs)
        print("AFTER")

    return wrapper


def before_and_after_3(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        value = func(*args, **kwargs)
        print("AFTER")
        return value

    return wrapper


#
# Exercise 2
#
def do_twice_1(func):
    def wrapper(*args, **kwargs):
        return func(*args, *kwargs), func(*args, **kwargs)

    return wrapper


def do_twice(func):
    def wrapper(*args, **kwargs):
        first = func(*args, **kwargs)
        second = func(*args, **kwargs)
        return first, second

    return wrapper


# Example of using * operator to allow varying number of parameters
def adder(number, *numbers):
    if not numbers:
        return number
    return number + adder(*numbers)


def before_and_after_4(func):
    print(f"Decorating {func.__name__}")

    def wrapper(*args, **kwargs):
        print("BEFORE")
        value = func(*args, **kwargs)
        print("AFTER")
        return value

    return wrapper


def before_and_after(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("BEFORE")
        value = func(*args, **kwargs)
        print("AFTER")
        return value

    return wrapper


#
# Exercise 3
#
FUNCTIONS = {}


def register(func):
    FUNCTIONS[func.__name__] = func
    return func


#
# Exercise 4
#
def retry_1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception:
                pass

    return wrapper


def retry_2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Retrying {func.__name__} because of {e}")
                time.sleep(0.1)

    return wrapper


#
# Exercise 6
#
def retry_3(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries - 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying {func.__name__} ({e})")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_4(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying {func.__name__} ({e})")
            else:
                print(f"{max_retries} retries done")

        return wrapper

    return decorator


def retry(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries - wrapper.num_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"{wrapper.num_retries}: Retrying {func.__name__} ({e})")
                    wrapper.num_retries += 1
            else:
                print(f"{max_retries} retries done")

        wrapper.num_retries = 0
        return wrapper

    return decorator
