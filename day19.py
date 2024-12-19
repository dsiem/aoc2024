import functools


@functools.cache
def combinations(design, count=0):
    if not design:
        return 1
    for pattern in patterns:
        if design.startswith(pattern):
            count += combinations(design[len(pattern) :])
    return count


patterns, _, *designs = open(0).read().splitlines()
patterns = patterns.split(", ")
print(*map(sum, zip(*((cnt > 0, cnt) for cnt in (combinations(design) for design in designs)))))
