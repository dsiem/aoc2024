import re
from collections.abc import Iterable


def ints(s: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", s)))


def tokens(machine: Iterable[int], offset: int = 0) -> int:
    ax, ay, bx, by, px, py = machine
    px += offset
    py += offset
    di = ax * by - ay * bx
    an, ar = divmod(px * by - py * bx, di)
    bn, br = divmod(py * ax - px * ay, di)
    return (ar == br == 0) * (3 * an + bn)


machines = map(ints, open(0).read().split("\n\n"))
print(*map(sum, zip(*((tokens(machine), tokens(machine, 10000000000000)) for machine in machines))))
