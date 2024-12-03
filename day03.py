import re
from math import prod

input = f"{open(0).read()}do()"
mul = lambda s: sum(map(lambda pair: prod(map(int, pair)), re.findall(r"mul\((\d+),(\d+)\)", s)))
print(mul(input), mul(re.sub(r"(?s)don't\(\)(.*?)do\(\)", "", input)))
