from functools import cache


@cache
def recursive_fibonacci(n):
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2) if n > 1 else n


def run(iterations):
    for n in range(iterations):
        print(n, recursive_fibonacci(n))


if __name__ == '__main__':
    run(1000)
