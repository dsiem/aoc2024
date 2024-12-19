def cmp(a: int, b: int) -> int:
    return 1 + (a > b) - (a < b)


w, h = 101, 103
robots = [0] * 9
states = [[int(n) for col in line.split() for n in col[2:].split(",")] for line in open(0)]
safety_100, safety_x, safety_y = 0, (1 << 32, 0), (1 << 32, 0)

for n in range(max(w, h)):
    robots[:] = [0] * 9
    for x, y, vx, vy in states:
        robots[cmp((x + n * vx) % w, w // 2) + 3 * cmp((y + n * vy) % h, h // 2)] += 1
    safety_100 += (n == 100) * robots[0] * robots[2] * robots[6] * robots[8]
    safety_x = _, nx = min(safety_x, ((robots[0] + robots[6]) * (robots[2] + robots[8]), n))
    safety_y = _, ny = min(safety_y, ((robots[0] + robots[2]) * (robots[6] + robots[8]), n))

print(safety_100, nx + pow(w, -1, h) * (ny - nx) % h * w)
