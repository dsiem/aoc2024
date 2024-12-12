import itertools


def part1(blocks: list[int]) -> int:
    disk = {}
    pos = 0
    for id, (used, empty) in enumerate(zip(blocks[::2], blocks[1::2] + [0])):
        disk |= {pos + inner: id for inner in range(used)}
        pos += used + empty
    positions = list(disk)
    return sum(i * disk[i if i in disk else positions.pop()] for i in range(len(disk)))


def part2(blocks: list[int]) -> int:
    start = [0, *list(itertools.accumulate(blocks))][::2]
    empty = blocks[1::2]
    checksum, *min_id = [0] * 11
    for id, (length, position) in reversed(list(enumerate(zip(blocks[::2], start)))):
        for i in range(max(min_id[: length + 1]), id):
            if empty[i] >= length:
                position = start[i + 1] - empty[i]
                empty[i] -= length
                break
        min_id[length] = i
        checksum += id * length * (length - 1 + 2 * position) // 2
    return checksum


blocks = list(map(int, open(0).read().strip()))
print(part1(blocks), part2(blocks))
