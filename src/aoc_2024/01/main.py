from collections import Counter
from pathlib import Path

data = Path("input.txt").read_text()

left: list[int] = []
right: list[int] = []
for line in data.splitlines():
    first, second = line.split()
    left.append(int(first))
    right.append(int(second))

left.sort()
right.sort()

res = sum(abs(a - b) for a, b in zip(left, right, strict=True))
print(res)


right_counts = Counter(right)

counts = sum(a * right_counts[a] for a in left)
print(counts)
