from typing import List

lines = [line.strip() for line in open("input.txt","r")]

print(lines[:20])

bags:List[str] = [[]]
i: int = 0

for item in lines:
    if not item:
        i += 1
        bags.append([])
        continue
    bags[i].append(int(item))

elf_cals = [sum(cal) for cal in bags]
print(max(elf_cals)) # Part 1 ans

elf_cals.sort(reverse=True)
print(elf_cals[:3])
print(sum(elf_cals[:3]))

