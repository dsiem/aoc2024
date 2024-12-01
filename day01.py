import collections

fst, snd = map(sorted, zip(*(map(int, line.split()) for line in open(0))))
cnt = collections.Counter(snd)
print(*map(sum, zip(*((abs(a - b), a * cnt[a]) for a, b in zip(fst, snd)))))
