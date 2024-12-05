import collections
import graphlib

rules, updates = (s.split() for s in open(0).read().split("\n\n"))
rules, updates = [s.split("|") for s in rules], [s.split(",") for s in updates]

graph = collections.defaultdict(set)
for pred, succ in rules:
    graph[succ].add(pred)

part1 = part2 = 0
for update in updates:
    depend = {k: v & set(update) for k, v in graph.items() if k in update}
    sorted = list(graphlib.TopologicalSorter(depend).static_order())
    middle = int(sorted[(len(sorted) - 1) // 2])
    if sorted == update:
        part1 += middle
    else:
        part2 += middle

print(part1, part2)
