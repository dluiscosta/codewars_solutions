import functools


@functools.lru_cache(maxsize=None)
def height(n, m):
    if n == 0 or m == 0:
        return 0
    else:
        return sum([height(n-1, j) + 1 for j in range(m)])
