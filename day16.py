import heapq


grid = {complex(i, j): c for i, line in enumerate(open(0)) for j, c in enumerate(line.strip())}
start = next(pos for pos, c in grid.items() if c == "S")

best_paths = set()
best_score = 1 << 32
heap, seen = [(0, 0, start, 1j, {start})], {}

while heap:
    score, _, pos, dir, path = heapq.heappop(heap)
    if grid[pos] == "E" and score <= best_score:
        best_score = score
        best_paths |= path
    if (pos, dir) in seen and seen[(pos, dir)] < score:
        continue
    seen[(pos, dir)] = score
    for inc, dir_ in (1, dir), (1001, 1j * dir), (1001, -1j * dir):
        pos_ = pos + dir_
        if grid[pos_] != "#":
            heapq.heappush(heap, (score + inc, id(pos_), pos_, dir_, path | {pos_}))

print(best_score, len(best_paths))
