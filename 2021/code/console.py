# Introductory example

import time


def slow_square(number):
    print(f"Sleeping for {number} seconds")
    time.sleep(number)
    return number ** 2


slow_square(3)  # Super slow ...


from functools import lru_cache


@lru_cache
def slow_square(number):
    print(f"Sleeping for {number} seconds")
    time.sleep(number)
    return number ** 2


slow_square(3)
slow_square(3)  # Cached
slow_square(2)  # Not cached, new parameter
slow_square(2)  # Cached

# Functions can be assigned to variables
print
skriv_ut = print  # skriv_ut is Norwegian for print
skriv_ut("Hi PyCon!")
skriv_ut


# Functions can be passed in as parameters
def greet(name, printer=print):
    printer(f"Hi {name}!")


greet("PyCon")


def tnirp(text):
    print(text[::-1])


greet("PyCon", printer=tnirp)


# Functions can be dynamically defined (function factories)
def prefix_factory(prefix):
    def prefix_printer(text):
        print(f"{prefix}: {text}")
    return prefix_printer


debug = prefix_factory("DEBUG")
debug
debug("Hi PyCon!")
greet("PyCon", printer=debug)


# We can pass in functions to function factories
def reverse_factory(func):
    def reverse_caller(text):
        func(text[::-1])
    return reverse_caller


reverse_print = reverse_factory(print)
reverse_print("Hi PyCon!")
reverse_tnirp = reverse_factory(tnirp)
reverse_tnirp("Hi PyCon!")
reverse_debug = reverse_factory(debug)
reverse_debug("Hi Pycon!")

# reverse_factory is a decorator!
def greet(name):
    print(f"Hi {name}!")


greet("PyCon")


@reverse_factory
def greet(name):
    print(f"Hi {name}!")


greet("PyCon")


# The @-syntax is just syntactic sugar
@reverse_factory
def greet(name):
    print(f"Hi {name}!")


def greet(name):
    print(f"Hi {name}!")

greet = reverse_factory(greet)


# Exercise 1: Decorators typically do something before and after calling the
# decorated function
def before_and_after(func):
    def wrapper(text):
        print("BEFORE")
        func(text)
        print("AFTER")
    return wrapper


@before_and_after
def greet(name):
    print(f"Hi {name}!")


greet("PyCon")


# Handling different function arguments with *args and **kwargs
def adder(number_1, number_2):
    return number_1 + number_2


@before_and_after
def adder(number_1, number_2):
    return number_1 + number_2


adder(3, 10)  # Gives an error, @before_and_after is designed for 1 parameter


def params(*args, **kwargs):
    print(f"{args = }")
    print(f"{kwargs = }")


params()
params(1, 2, pycon=2021)


def before_and_after(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        func(*args, **kwargs)
        print("AFTER")
    return wrapper


@before_and_after
def adder(number_1, number_2):
    return number_1 + number_2


adder(3, 10)  # No error, but return value is lost


# Pass through return values
def before_and_after(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        value = func(*args, **kwargs)
        print("AFTER")
        return value
    return wrapper


@before_and_after
def adder(number_1, number_2):
    return number_1 + number_2


adder(3, 10)
result = adder(3, 10)
result


# Exercise 2
import random


def do_twice(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs), func(*args, **kwargs)
    return wrapper


@do_twice
def roll_dice():
    return random.randint(1, 6)


roll_dice()
roll_dice()


def do_twice(func):  # Alternative, more readable implementation
    def wrapper(*args, **kwargs):
        first = func(*args, **kwargs)
        second = func(*args, **kwargs)
        return first, second
    return wrapper


# Decorators that only do something at define time
def define(func):
    print(f"Defining {func.__name__}")
    return func


@define
def roll_dice():
    return random.randint(1, 6)


roll_dice()
roll_dice()


# Exercise 3
def register(func):
    FUNCTIONS[func.__name__] = func
    return func


FUNCTIONS = {}


@register
def roll_dice():
    return random.randint(1, 6)


FUNCTIONS
FUNCTIONS["roll_dice"]
FUNCTIONS["roll_dice"]()

func_name = input("Which function do you want to call?")
FUNCTIONS[func_name]()


# Stacking decorators
@do_twice
@do_twice
def roll_dice():
    return random.randint(1, 6)


roll_dice()


@register
@do_twice
def roll_dice():
    return random.randint(1, 6)


FUNCTIONS
FUNCTIONS["roll_dice"]()
FUNCTIONS["wrapper"]()


# Handling metadata of decorated functions with @functools.wraps
import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        first = func(*args, **kwargs)
        second = func(*args, **kwargs)
        return first, second
    return wrapper


@do_twice
def roll_dice():
    return random.randint(1, 6)

roll_dice
FUNCTIONS = {}


@register
@do_twice
def roll_dice():
    return random.randint(1, 6)


FUNCTIONS

roll_dice.__wrapped__  # You can access the original function through __wrapped__
roll_dice.__wrapped__()
roll_dice()


# The order of stacked decorators may be important
@do_twice
@before_and_after
def greet(name):
    print(f"Hi {name}!")


greet("PyCon")


@before_and_after
@do_twice
def greet(name):
    print(f"Hi {name}!")


greet("PyCon")


# Exercise 4
def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception:
                pass
    return wrapper


@retry
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


only_roll_sixes()
only_roll_sixes()

def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Retrying ({e})")  # Add visibility to what's going on
    return wrapper


@retry
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


only_roll_sixes()


# Use @retry for a simple file system poller
@retry
def process_file(path):
    print(path.read_text())


import pathlib
process_file(pathlib.Path("pycon.txt"))


# Use @retry for simple validation of input
@retry
def get_age():
    return int(input("How old are you? "))


get_age()
get_age()


# Exercise 5: Decorators with parameters - define decorator factories
def retry(exception):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ...
        return wrapper
    return decorator


@retry(ValueError)
def calculation():
    ...


calculation = retry(ValueError)(calculation)


def retry(exception):
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


@retry(ValueError)
def calculation():
    number = random.randint(-5, 5)
    if abs(1 / number) > 0.2:
        raise ValueError(number)
    return number


calculation()
calculation()


# Exercise 6
def retry(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying ({e})")
        return wrapper
    return decorator


@retry(max_retries=3)
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


only_roll_sixes()
only_roll_sixes()


def retry(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying ({e})")
            return func(*args, **kwargs)  # Add final call to raise error
        return wrapper
    return decorator


@retry(max_retries=3)
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


only_roll_sixes()
only_roll_sixes()
only_roll_sixes()


# Keep state for decorators
RETRIES = {}  # Could use a global dictionary, like we did for @register, but
              # better to use attributes on the function
only_roll_sixes.__wrapped__


def retry(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying ({e})")
            return func(*args, **kwargs)
        wrapper.num_retries = 0
        return wrapper
    return decorator


@retry(max_retries=3)
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


only_roll_sixes
only_roll_sixes.num_retries


def retry(max_retries):
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


@retry(max_retries=10)
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


only_roll_sixes()
only_roll_sixes.num_retries
only_roll_sixes()
only_roll_sixes()


# Use classes as decorators in order to keep state
def before_and_after(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        value = func(*args, **kwargs)
        print("AFTER")
        return value
    return wrapper


class BeforeAndAfter:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
    def __call__(self, *args, **kwargs):
        print("BEFORE")
        value = self.func(*args, **kwargs)
        print("AFTER")
        return value


@BeforeAndAfter
def greet(name):
    print(f"Hi {name}!")


greet("PyCon")

BeforeAndAfter(greet)
type(greet)
type(roll_dice)


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
            except Exception as e:
                self.num_retries += 1
                print(f"Retry attempt {self.num_retries}")


@Retry
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


only_roll_sixes
only_roll_sixes.num_retries
only_roll_sixes()
only_roll_sixes.num_retries
only_roll_sixes()
only_roll_sixes()
