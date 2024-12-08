import itertools
from collections.abc import Iterable


def solve(multipliers: Iterable[int]) -> int:
    antinodes = set()
    for (p, u), (q, v) in itertools.combinations(grid.items(), 2):
        if u == v != ".":
            antinodes |= {a for m in multipliers if (a := p + m * (q - p)) in grid}
    return len(antinodes)


grid = {complex(i, j): c for i, line in enumerate(open(0)) for j, c in enumerate(line.strip())}
size = max(int(max(z.real, z.imag)) for z in grid)
print(*(solve(multipliers) for multipliers in ((-1, 2), range(-size, size + 1))))
