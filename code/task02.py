import random

from pycon_decorators import trace


GREETINGS = ["Heisann", "Hi there", "Ni!"]


@trace
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"


@trace
def random_greet(name="Emily"):
    greeting = random.choice(GREETINGS)
    return greet(name, greeting=greeting)


@trace
def greet_many(number):
    return [random_greet() for _ in range(number)]
