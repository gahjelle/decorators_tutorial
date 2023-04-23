#
# Introduction
#

import time


def slow_square(number):
    print(f"Sleeping for {number} seconds")
    time.sleep(number)
    return number**2


slow_square(3)  # Slow ...
slow_square(3)  # Still slow ...

from functools import cache

# "Manual" decoration
cached_square = cache(slow_square)

cached_square(3)  # Slow ...
cached_square(3)  # Fast!
cached_square(2)  # Slow ...
cached_square(2)  # Fast!
cached_square(3)  # Still fast!

# Regular decorator syntax
@cache
def cached_square(number):
    print(f"Sleeping for {number} seconds")
    time.sleep(number)
    return number**2


cached_square(3)  # Slow ...
cached_square(3)  # Fast!

#
# Functions
#


def double(x):
    return x * 2


double  # Reference to function object, no parentheses
double(234)  # Call function by adding parentheses

skriv_ut = print  # Functions are objects, you can assign other names
skriv_ut  # Reference to the print() function
skriv_ut("Hi, PyCon!")  # Call print() through the new name

print = 3  # A regular variable "overwrites" the function reference
print

del print  # Restore the built-in print() function
print
print(2 + 3)

# Functions can be passed as arguments
def greet(name, greeter):
    greeter(f"Hi, {name}!")


greet("PyCon", greeter=print)
greet("PyCon", greeter=skriv_ut)

# Define a backwards print() function for demo purposes
def tnirp(text):
    print(text[::-1])


tnirp("Hi there!")
greet("PyCon", greeter=tnirp)

# Factory functions can create new functions dynamically
def prefix_factory(prefix):
    def prefix_printer(text):
        print(f"{prefix}: {text}")

    return prefix_printer


# prefix_printer("Hi")  # prefix_printer() is not in scope and can't be called

debug = prefix_factory("DEBUG")
debug("Hi, PyCon!")
debug("Something else")
greet("PyCon", greeter=debug)

warning = prefix_factory("WARNING")
warning("Oops!")

# Factory functions can be parametrized by other functions
def reverse_factory(func):
    def reverse_caller(text):
        func(text[::-1])

    return reverse_caller


reverse_print = reverse_factory(print)
reverse_print("Hi, PyCon!")

reverse_tnirp = reverse_factory(tnirp)
reverse_tnirp("Hi, PyCon!")

reverse_debug = reverse_factory(debug)
reverse_debug("Hi, PyCon!")

# reverse_factory() is a decorator, apply it!
def hi(name):
    print(f"Hi, {name}!")


hi("PyCon")

hi = reverse_factory(hi)  # Manual decoration
hi("PyCon")

# Regular decorator syntax
@reverse_factory
def hello(name):
    print(f"Hello, {name}!")


hello("PyCon")

#
# Exercise 1
#
def before_and_after(func):
    def wrapper(text):
        print("BEFORE")
        func(text)
        print("AFTER")

    return wrapper


@before_and_after
def hi(name):
    print(f"Hi, {name}!")


hi("PyCon")

# @before_and_after is limited in which functions it can decorate
def adder(number_1, number_2):
    return number_1 + number_2


adder(23, 10)  # Adds two numbers


@before_and_after
def adder(number_1, number_2):
    return number_1 + number_2


# adder(23, 10)  # Doesn't work because wrapper() expects one argument

# Use *args and **kwargs for a flexible number of parameters
def params(*args, **kwargs):
    print(f"{args = }")
    print(f"{kwargs = }")


params("Hi PyCon")
params(greeting="Hi PyCon")
params(3.14, greeting="Hi PyCon")
params(3.14, 23, greeting="Hi PyCon")
params(3.14, 23, "Geir Arne", greeting="Hi PyCon", e=2.7128)

# Use *args to create a flexible adder() that can handle any number of arguments
def adder(number, *numbers):
    if not numbers:
        return number
    return number + adder(*numbers)


adder(23)
adder(23, 10)
adder(23, 10, 78)

# Define a more flexible decorator
def before_and_after(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        func(*args, **kwargs)
        print("AFTER")

    return wrapper


@before_and_after
def adder(number_1, number_2):
    return number_1 + number_2


adder(23, 10)  # Doesn't crash, but doesn't return the answer!

# Handle return values
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


adder(23, 10)  # Works!

#
# Exercise 2
#
import random


def do_twice(func):
    def wrapper(*args, **kwargs):
        return func(*args, *kwargs), func(*args, **kwargs)

    return wrapper


@do_twice
def roll_dice():
    return random.randint(1, 6)


roll_dice()
roll_dice()

# More readable by spelling out each function invocation
def do_twice(func):
    def wrapper(*args, **kwargs):
        first = func(*args, **kwargs)
        second = func(*args, **kwargs)
        return first, second

    return wrapper


@do_twice
def roll_dice():
    return random.randint(1, 6)


roll_dice()

# Stack decorators
@do_twice
@before_and_after
def roll_dice():
    return random.randint(1, 6)


roll_dice()

# The order of decorators matter
@before_and_after
@do_twice
def roll_dice():
    return random.randint(1, 6)


roll_dice()

# You can also apply the same decorator several times
@do_twice
@do_twice
def roll_dice():
    return random.randint(1, 6)


roll_dice()

# Code outside wrapper() is executed when a decorated function is defined
def before_and_after(func):
    print(f"Decorating {func.__name__}")

    def wrapper(*args, **kwargs):
        print("BEFORE")
        value = func(*args, **kwargs)
        print("AFTER")
        return value

    return wrapper


@before_and_after
def hi(name):
    print(f"Hi, {name}!")


hi("PyCon")

# If a decorator only does something at "define-time", you don't need wrapper()
def define(func):
    print(f"Decorating {func.__name__}")
    return func


@define
def hi(name):
    print(f"Hi, {name}!")


hi("PyCon")

#
# Exercise 3
#
def register(func):
    FUNCTIONS[func.__name__] = func
    return func


FUNCTIONS = {}


@register
def dice_roll():
    return random.randint(1, 6)


FUNCTIONS
FUNCTIONS["dice_roll"]
FUNCTIONS["dice_roll"]()
FUNCTIONS["dice_roll"]()

dice_roll

# You should return a function, otherwise you can't use the decorated function
FUNCTIONS = {}


def register(func):
    FUNCTIONS[func.__name__] = func


@register
def dice_roll():
    return random.randint(1, 6)


FUNCTIONS
FUNCTIONS["dice_roll"]()
FUNCTIONS["dice_roll"]()

print(dice_roll)  # None, because @register didn't explicitly return

# dice_roll()  # Doesn't work because dice_roll is None

# Dynamically choose which function to call
name = input("Which function do you want to call? ")
FUNCTIONS[name]()

# Inspect metadata (like the name) of a function
def hi(name):
    print(f"Hi, {name}!")


@before_and_after
def hello(name):
    print(f"Hello, {name}!")


hello
hello.__name__

hi
hi.__name__

print
print.__name__

skriv_ut = print
skriv_ut
skriv_ut.__name__

# Use @functools.wraps to copy metadata
import functools


def before_and_after(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("BEFORE")
        value = func(*args, **kwargs)
        print("AFTER")
        return value

    return wrapper


@before_and_after
def hello(name):
    print(f"Hello, {name}!")


hello.__name__  # Proper name

# Refer to the undecorated function
hi.__wrapped__

hi("PyCon")
hi.__wrapped__("PyCon")

#
# Exercise 4
#
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
def only_roll_highs():
    number = random.randint(1, 6)
    if number < 5:
        raise ValueError(number)
    return number


only_roll_highs()
only_roll_highs()
only_roll_highs()

# Add a print() to show what's happening
def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Retrying {func.__name__} because of {e}")

    return wrapper


@retry
def only_roll_highs():
    number = random.randint(1, 6)
    if number < 5:
        raise ValueError(number)
    return number


only_roll_highs()
only_roll_highs()
only_roll_highs()

# Slow down rate of retries to avoid overloading the system
def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Retrying {func.__name__} because of {e}")
                time.sleep(0.1)

    return wrapper


@retry
def only_roll_highs():
    number = random.randint(1, 6)
    if number < 5:
        raise ValueError(number)
    return number


only_roll_highs()
only_roll_highs()
only_roll_highs()

# Use pathlib to poll for a file
import pathlib


@retry
def process_file(path):
    print(path.read_text())


process_file(pathlib.Path("pycon.txt"))  # Retries until it finds pycon.txt

# Basic validation of integer input
def get_age():
    return int(input("How old are you? "))


get_age()  # Crashes if the user enters a non-integer

# Retry until a valid integer is entered
@retry
def get_age():
    return int(input("How old are you? "))


get_age()

#
# Exercise 5 (skipped during tutorial)
#
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

#
# Exercise 6
#
def retry(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying {func.__name__} ({e})")

        return wrapper

    return decorator


@retry(max_retries=2)
def only_roll_highs():
    number = random.randint(1, 6)
    if number < 5:
        raise ValueError(number)
    return number


only_roll_highs()
only_roll_highs()
only_roll_highs()


def retry(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries - 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying {func.__name__} ({e})")
            return func(*args, **kwargs)  # Add unprotected return to raise at end

        return wrapper

    return decorator


@retry(max_retries=2)
def only_roll_highs():
    number = random.randint(1, 6)
    if number < 5:
        raise ValueError(number)
    return number


only_roll_highs()
only_roll_highs()
only_roll_highs()

#
# Exercise 6 challenge
#
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


@retry(max_retries=10)
def only_roll_highs():
    number = random.randint(1, 6)
    if number < 5:
        raise ValueError(number)
    return number


only_roll_highs()
only_roll_highs()
only_roll_highs()
only_roll_highs.num_retries

only_roll_highs()
only_roll_highs()
only_roll_highs()

# Use classes as decorators in order to keep state
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
def hi(name):
    print(f"Hi, {name}!")


hi("PyCon")

#
# Exercise 7 (skipped during tutorial)
#
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
def only_roll_highs():
    number = random.randint(1, 6)
    if number < 5:
        raise ValueError(number)
    return number


only_roll_highs
only_roll_highs.num_retries
only_roll_highs()
only_roll_highs.num_retries
only_roll_highs()
only_roll_highs()


#
# Exercise 8 (skipped during tutorial)
#
def enforce(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for name, value in kwargs.items():
            if not isinstance(value, annotation := func.__annotations__[name]):
                raise TypeError(f"{name} should be {annotation}")
        return func(*args, **kwargs)

    return wrapper


@enforce
def adder(number_1: int, number_2: int) -> int:
    return number_1 + number_2


adder(number_1=23, number_2=10)  # Returns 33
# adder(number_1=3.14, number_2=2.71)  # Raises TypeError
