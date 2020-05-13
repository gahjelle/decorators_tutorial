# Introduction to Decorators - Tutorial given at PyCon Online 2020

This repository contains supporting material for the **Introduction to Decorators - Power Up Your Python Code** tutorial I presented at the [Pycon Online 2020](https://us.pycon.org/2020/online/) conference.

The tutorial is available as a video on [YouTube](https://www.youtube.com/watch?v=T8CQwGIsrx4). 


## Exercises

The course is organized around 6 different exercises that show different techniques for constructing decorators in Python. For each exercise, your task is to implement a decorator that makes the given code run properly. The code for each exercise is available below:

- [Exercise 1](code/task01.py): Your first decorator: `@timer`
- [Exercise 2](code/task02.py): A decorator that use the function arguments: `@trace`
- [Exercise 3](code/task03.py): A decorator that don't wrap the original function: `@register`
- [Exercise 4](code/task04.py): A decorator that keep state: `@count_calls`
- [Exercise 5](code/task05.py): A decorator with arguments: `@use_units`
- [Exercise 6](code/task06.py): A decorator with optional arguments: `@supertrace`

See the table of contents below for links to each exercise in the video.


## Tutorial Content

The tutorial is divided into four main sections. Each of these explain several concepts, and give you some exercises to work through. I recommend that you code along during the video, and stop the video when necessary - and in particular for the exercises - to try out code for your self.

The following list contains links directly to the different sections in the video:

- [0:00](https://www.youtube.com/watch?v=T8CQwGIsrx4): Introduction (3 min)

- [3:32](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=3m32s): Getting Started (45 min)
    - [7:06](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=7m06s): Functions are First-Class Objects (8 min)
    - [15:17](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=15m17s): Inner Functions (9 min)
    - [24:18](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=24m18s): Wrapping Functions (2 min)
    - [26:26](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=26m26s): Decorating Functions (7 min)
    - [33:15](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=33m15s): Making Decorators Play Nice (15 min)

- [48:42](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=48m42s): Basic Decorators (43 min)
    - [49:52](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=49m52s): Task 1: `@timer` (4 min)
    - [54:40](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=54m40s): Task 1: Solution (4 min)
    - [59:07](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=59m07s): Task 2: `@trace` (5 min)
    - [1:04:22](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=64m22s): Task 2: Solution (9 min)
    - [1:13:44](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=73m44s): Stacking Decorators (4 min)
    - [1:17:21](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=77m21s): Task 3: `@register` (8 min)
    - [1:25:02](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=85m02s): Task 3: Solution (7 min)

- [1:32:18](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=92m18s): Advanced Decorators (70 min)
    - [1:34:12](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=94m12s): Task 4: `@count_calls` (6 min)
    - [1:40:30](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=100m30s): Keeping State With Function Attributes (3 min)
    - [1:43:45](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=103m45s): Task 4: Solution (5 min)
    - [1:48:28](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=108m28s): Implementing a Decorator as a Class (12 min)
    - [2:00:57](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=120m57s): Decorators Applied to Classes (10 min)
    - [2:11:32](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=131m32s): Decorators With Arguments (13 min)
    - [2:24:30](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=144m30s): Task 5: `@use_units` (7 min)
    - [2:31:24](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=151m24s): Task 5: Solution (8 min)
    - [2:39:42](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=159m42s): Task 6: `@supertrace` (3 min)
    - [2:42:08](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=162m08s): Decorators With Optional Arguments (5 min)
    - [2:47:11](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=167m11s): Task 6: Solution (16 min)

- [3:03:53](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=183m53s): Conclusion (18 min)
    - [3:04:40](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=184m40s): Decorating External Functions (5 min)
    - [3:09:48](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=189m48s): Decorators in the Wild (3 min)
    - [3:12:48](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=192m48s): Further Resources (3 min)
    - [3:15:44](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=195m44s): PEP 614 - More Flexible Decorators (4 min)
    - [3:20:40](https://www.youtube.com/watch?v=T8CQwGIsrx4&t=200m40s): Contact (1 min)


## Further Resources

- Real Python article: [realpython.com/primer-on-python-decorators](https://realpython.com/primer-on-python-decorators)
- Real Python video course: [realpython.com/courses/python-decorators-101](https://realpython.com/courses/python-decorators-101)
- `decorator` package: [pypi.org/project/decorator](https://pypi.org/project/decorator)
- Python Cookbook: [github.com/dabeaz/python-cookbook/tree/master/src/9](https://github.com/dabeaz/python-cookbook/tree/master/src/9)
- PEP 318: [www.python.org/dev/peps/pep-0318](https://www.python.org/dev/peps/pep-0318)
- PEP 614: [www.python.org/dev/peps/pep-0614](https://www.python.org/dev/peps/pep-0614)
