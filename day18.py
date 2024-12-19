import heapq


def search(wait: int) -> list[int]:
    heap, seen = [(0, (0, 0), [])], set()
    while heap:
        steps, pos, path = _, (x, y), _ = heapq.heappop(heap)
        if pos == stop:
            return path
        if pos in seen:
            continue
        seen.add(pos)
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            pos_ = x_, y_ = (x + dx, y + dy)
            if 0 <= x_ <= stop[0] and 0 <= y_ <= stop[1] and pos_ not in bytes[:wait]:
                heapq.heappush(heap, (steps + 1, pos_, path + [pos_]))


bytes = [tuple(map(int, line.split(","))) for line in open(0)]
stop, wait = (70, 70), 1024
path = search(wait)
steps = len(path)

while path:
    wait = next(n + 1 for n, byte in enumerate(bytes[wait:], wait) if byte in path)
    path = search(wait)

print(steps, ",".join(map(str, bytes[wait - 1])))
