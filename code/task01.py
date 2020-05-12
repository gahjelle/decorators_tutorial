from pycon_decorators import timer


@timer
def waste_time(number):
    total = 0
    for num in range(number):
        total += sum(n for n in range(num))
    return total
