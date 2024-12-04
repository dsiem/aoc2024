input = open(0).readlines()

part1 = 0
ds = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
for i, line in enumerate(input):
    for j, letter in enumerate(line):
        if letter != "X":
            continue
        for di, dj in ds:
            if (
                i + 3 * di < 0
                or i + 3 * di >= len(input)
                or j + 3 * dj < 0
                or j + 3 * dj >= len(line)
            ):
                continue
            for n, other_letter in enumerate("MAS", 1):
                if input[i + n * di][j + n * dj] != other_letter:
                    break
            else:
                part1 += 1
print(part1)

part2 = 0
ds = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
for i, line in enumerate(input[1:-1], 1):
    for j, letter in enumerate(line[1:-1], 1):
        if letter != "A":
            continue
        count = 0
        for di, dj in ds:
            for n, other_letter in enumerate("MS"):
                m = n * 2 - 1
                if input[i + m * di][j + m * dj] != other_letter:
                    break
            else:
                count += 1
        if count == 2:
            part2 += 1
print(part2)
