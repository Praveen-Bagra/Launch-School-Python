from time import perf_counter
from functools import lru_cache

def time_runs(func):
    """Decorator that times how long it takes to run the function 'func'"""
    def wrapper(*args, **kwargs):
        start = perf_counter()
        return_value = func(*args, **kwargs)
        print(f'The function ran in {perf_counter() - start} seconds')
        return return_value

    return wrapper

@time_runs
@lru_cache
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

print(is_prime(73729261))
print()
print(is_prime(73729261))

