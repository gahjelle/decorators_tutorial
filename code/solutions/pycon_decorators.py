import functools
import time
import pint

REGISTERED = {}


def register(func):
    """Register a function"""
    REGISTERED[func.__name__] = func
    return func


def timer(func):
    """Timing a function"""

    @functools.wraps(func)
    def _timer(*args, **kwargs):
        """The timer function replacing the original"""
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        print(f"Elapsed time: {toc - tic:.2f} seconds")
        return value

    return _timer


def trace(func):
    """Show the trace of function calls"""
    name = func.__name__

    @functools.wraps(func)
    def _trace(*args, **kwargs):
        """The trace function that replaces the original"""
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {name}({signature})")
        value = func(*args, **kwargs)
        print(f"{name} returned {value!r}")
        return value

    return _trace


def count_calls(func):
    """Count the number of calls to a function"""

    @functools.wraps(func)
    def _count_calls(*args, **kwargs):
        _count_calls.num_calls += 1
        return func(*args, **kwargs)

    _count_calls.num_calls = 0
    return _count_calls


class CountCalls:
    """Count the number of calls to a function"""

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        return self.func(*args, **kwargs)


def use_unit(unit):
    """Add units to return values"""
    use_unit.ureg = pint.UnitRegistry()

    def _use_unit_decorator(func):
        @functools.wraps(func)
        def _use_unit(*args, **kwargs):
            return func(*args, **kwargs) * use_unit.ureg(unit)

        _use_unit.unit = unit
        return _use_unit

    return _use_unit_decorator


def supertrace(func=None, *, logger=print):
    def _supertrace_decorator(func):
        """Show the trace of function calls"""
        name = func.__name__

        @functools.wraps(func)
        def _supertrace(*args, **kwargs):
            """The trace function that replaces the original"""
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            logger(f"Calling {name}({signature})")
            value = func(*args, **kwargs)
            logger(f"{name} returned {value!r}")
            return value

        return _supertrace

    if func is None:
        return _supertrace_decorator
    else:
        return _supertrace_decorator(func)
