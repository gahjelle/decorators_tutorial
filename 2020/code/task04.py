from pycon_decorators import CountCalls


@CountCalls
def fibonacci(number):
    """Calculate Fibonacci numbers fib_n

    The Fibonacci numbers are 1, 2, 3, 5, 8, 13, 21, ...

      fib_n = fib_n-1 + fib_n-2
    """
    if number < 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)
