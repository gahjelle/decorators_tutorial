import logging
import random

from pycon_decorators import supertrace

GREETINGS = ["Heisann", "Hi there", "Ni!"]


@supertrace
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"


@supertrace(logger=logging.warning)
def random_greet(name="Emily"):
    greeting = random.choice(GREETINGS)
    return greet(name, greeting=greeting)
