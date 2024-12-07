def walk(obstruction=-1):
    pos, dir, seen = start, -1, set()
    while pos in grid and (pos, dir) not in seen:
        seen.add((pos, dir))
        if grid.get(pos + dir) == "#" or pos + dir == obstruction:
            dir *= -1j
        else:
            pos += dir
    return seen, pos in grid


grid = {complex(i, j): c for i, line in enumerate(open(0)) for j, c in enumerate(line.strip())}
start = next(p for p, c in grid.items() if c == "^")
path = {pos for pos, _ in walk()[0]}
print(len(path), sum(is_cycle for _, is_cycle in map(walk, path)))
