import itertools
import operator


def _is_safe(report):
    diffs = set(map(operator.sub, report, report[1:]))
    return diffs <= {1, 2, 3} or diffs <= {-1, -2, -3}


def is_safe(report):
    return (_is_safe(report), any(map(_is_safe, itertools.combinations(report, len(report) - 1))))


print(*map(sum, zip(*(is_safe(list(map(int, line.split()))) for line in open(0)))))
