# Introduction to Decorators - Tutorial given at PyCon Online 2021

This repository contains supporting material for the **Introduction to Decorators - Power Up Your Python Code** tutorial I presented at the [Pycon Online 2021](https://us.pycon.org/2021/) conference.

The tutorial is available as a video on [YouTube](https://youtu.be/VWZAh1QrqRE). Thanks to PyCon for allowing me to present, and thanks to Ben and Diane for hosting and for captioning the video.


## Exercises

The tutorial is centered around several exercises asking you to implement different decorators, and reinforcing concepts introduced during the tutorial. Please see the video for full context. The exercises are available as [PDF-slides](exercises.pdf), and also listed below. Solutions to the exercises are available in the [Code-section](#code).

### Exercise 1

Write a decorator that prints `BEFORE` before calling the decorated function and `AFTER` afterwards.

```python
>>> @before_and_after
... def greet(name):
...     print(f"Hi {name}!")
...
>>> greet("PyCon")
BEFORE
Hi PyCon!
AFTER
```

### Exercise 2

Write a decorator that runs the decorated function twice and returns a 2-tuple with both return values.

```python
>>> import random
>>> @do_twice
... def roll_dice():
...     return random.randint(1, 6)
...
>>> roll_dice()
(3, 1)
```

### Exercise 3

Write a decorator that stores references to decorated functions in a dictionary.

```python
>>> FUNCTIONS = {}
>>> @register
... def roll_dice():
...     return random.randint(1, 6)
...
>>> FUNCTIONS
{'roll_dice': <function __main__.roll_dice()>}
>>> FUNCTIONS["roll_dice"]()
2
```

### Exercise 4

Write a decorator that repeatedly calls the decorated function as long as it raises an exception.

```python
>>> @retry
... def only_roll_sixes():
...     number = random.randint(1, 6)
...     if number != 6:
...         raise ValueError(number)
...     return number
...
>>> only_roll_sixes()
6
```

### Exercise 5 (hard)

Rewrite `@retry` so that it only retries on specific, user-defined exceptions.

```python
>>> @retry(ValueError)
... def calculation():
...     number = random.randint(-5, 5)
...     if abs(1 / number) > 0.2:
...         raise ValueError(number)
...     return number
...
>>> calculation()
# -5, 5, or ZeroDivisionError
```

### Exercise 6

Adapt `@retry` so that it only tries a maximum of `max_retries` times.

```python
>>> @retry(max_retries=3)
... def only_roll_sixes():
...     number = random.randint(1, 6)
...     if number != 6:
...         raise ValueError(number)
...     return number
...
>>> only_roll_sixes()
# 6 or ValueError
```

**Challenge:** Can you make `@retry` count all retries across several function calls?

### Exercise 7

Write a class-based `@Retry` decorator that keeps track of the number of retries across all function calls.

```python
>>> @Retry
... def only_roll_sixes():
...     number = random.randint(1, 6)
...     if number != 6:
...         raise ValueError(number)
...     return number
...
>>> only_roll_sixes()
Retry attempt 1
Retry attempt 2
6
>>> only_roll_sixes()
Retry attempt 3
6
```


## Code

All code was written live during the tutorial. You can download two files containing the code:

- [`console.py`](code/console.py): A slightly cleaned up version of the code written in the console during the tutorial
- [`decorators.py`](code/decorators.py): Functions and decorators copied over to the editor during the tutorial

Both files contain essentially the same code, including solutions to all exercises. The `console.py` file contains a bit more of the code used to run the examples as well.


## Resources

- Real Python articles:
    - [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators)
    - [Python Timer Functions: Three Ways to Monitor Your Code](https://realpython.com/python-timer/)
    - [Python 3.9: More Flexible Decorators](https://realpython.com/python39-new-features/#more-flexible-decorators)

- Real Python video course: [Python Decorators 101](https://realpython.com/courses/python-decorators-101/)

- Python Enhancement Proposals about decorators:
    - [PEP 318: Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
    - [PEP 3129: Class Decorators](https://www.python.org/dev/peps/pep-3129/)
    - [PEP 614: Relaxing Grammar Restrictions On Decorators](https://www.python.org/dev/peps/pep-0614/)

- Other resources:
    - [Awesome Python Decorator List](https://github.com/lord63/awesome-python-decorator)
    - [`tenacity` library with `@retry`-decorator](https://tenacity.readthedocs.io/)
