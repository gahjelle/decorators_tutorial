%title: Introduction to Decorators: Power Up Your Python Code
%author: PyCon Online 2020                  @gahjelle
%date: May 2020



-> # Geir Arne Hjelle <-




-> Amesto Nextbridge <-

-> _realpython.com_ <-

---

# Agenda

1. Introduction to Decorators
^

2. Basic Decorators - Exercises
^

3. Advanced Decorators - Exercises
^

4. Additional Resources

---

# Introduction to Decorators

- Functions are First Class Objects
^

- Inner Functions
^

- Manipulating Functions
^

- Decorating Functions
^

- Making Decorators Play Nice

---

# Advanced Decorators

- Keeping State
^

- Decorating Classes
^

- Adding Arguments
^

- Optional Arguments

---

# Key Take-aways

A **decorator** is any function that accepts a function and returns a function.
^


```
@wrapper
def function():
    ...
```

is just **syntactic sugar** for

```
def function():
    ...
function = wrapper(function)
```

---

# Key Take-aways (Continued)

- Use **function attributes** or **classes** to keep state.
^

- Decorators can take **arguments**. Implement this using **decorator factories**.
^

- Decorators can also **optionally** use arguments. In this case, your decorator
  factory need to return **either** a decorator or a wrapped function, depending
  on how it's called.

---

# Decorators Hall of Fame

- Standard Library:

    - @property
    - @classmethod
    - @staticmethod
    - @functools.wraps
    - @dataclasses.dataclass
    - @contextlib.contextmanager
^

- Notable Packages:
    - Numba: @jit
    - Flask: @app.route
    - Click: @command, @argument, @option

---

# Further Resources

- Real Python article: _realpython.com/primer-on-python-decorators_

- Real Python video course: _realpython.com/courses/python-decorators-101_

- decorator package: _pypi.org/project/decorator_

- Python Cookbook: _github.com/dabeaz/python-cookbook/tree/master/src/9_

- PEP 318: _www.python.org/dev/peps/pep-0318_

- PEP 614: _www.python.org/dev/peps/pep-0614_

---

-> # Thank You For Your Attention <-

^





-> - **Me:** @gahjelle                               <-
-> - **Code:** _github.com/gahjelle/decorators_tutorial_ <-
-> - **Real Python:** _realpython.com_                 <-

---

# Exercise






-> **Pause the video and implement your solution** <-
