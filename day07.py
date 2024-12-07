import functools
import itertools
import operator
import re


def ints(s: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", s)))


def concat(left: int, right: int) -> int:
    return int(f"{left}{right}")


def solve(operators, operands, result):
    first, *rest = operands
    for ops in itertools.product(operators, repeat=len(rest)):
        if functools.reduce(lambda acc, x: x[0](acc, x[1]), zip(ops, rest), first) == result:
            return True
    return False


part1 = part2 = 0
for result, *operands in map(ints, open(0)):
    if solve((operator.add, operator.mul), operands, result):
        part1 += result
    else:
        part2 += result * solve((concat, operator.add, operator.mul), operands, result)

print(part1, part1 + part2)
