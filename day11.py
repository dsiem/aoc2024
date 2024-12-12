import functools


@functools.cache
def blink(num: int, depth: int) -> int:
    if depth == 0:
        return 1
    if num == 0:
        return blink(1, depth - 1)
    if len(s := str(num)) % 2 == 0:
        digits = len(s)
        return blink(int(s[: digits // 2]), depth - 1) + blink(int(s[digits // 2 :]), depth - 1)
    return blink(num * 2024, depth - 1)


nums = list(map(int, open("day11.txt").read().split()))
print(*(sum(blink(n, d) for n in nums) for d in (25, 75)))
