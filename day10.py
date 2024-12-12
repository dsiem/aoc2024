def allowed(old: int, new: int) -> bool:
    return 0 <= new < len(grid) and -new % width != 1 and ord(grid[new]) - ord(grid[old]) == 1


def trails(queue: list[int]) -> tuple[int, int]:
    part1, part2 = set(), 0
    while queue:
        old = queue.pop()
        if grid[old] == "9":
            part1 |= {old}
            part2 += 1
        queue += [new for new in (old + 1, old - 1, old + width, old - width) if allowed(old, new)]
    return len(part1), part2


grid = open(0).read()
width = grid.find("\n") + 1
print(*map(sum, zip(*(trails([pos]) for pos, elevation in enumerate(grid) if elevation == "0"))))
