def fib(n):
    a, b = 0, 1
    while a < n:
        yield a     #yield - выдать, выдаем как return, но не выходим из функции
        a, b = b, a+b

gen = fib(10)
a = next(gen)
print(a)

generator = (i**2 for i in range(100))
sqr = [i**2 for i in range(100)]
print(next(generator))

#ДЕКОРАТОРЫ
from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def calculate_something(num):
    """
    Simple function that returns sum of all numbers up to the square of num.
    """
    total = sum((x for x in range(0, num**2)))
    return total

if __name__ == '__main__':
    calculate_something(10)
    calculate_something(100)
    calculate_something(1000)
    calculate_something(5000)
    calculate_something(10000)