lines = [line.strip() for line in open("input.txt","r")]

total_overlap_count = 0
partial_overlap_count = 0

for num, row in enumerate(lines): 
    ass_pair = row.split(",")
    ass_sets = list(map(lambda ass: set(sec for sec in range(int(ass.split("-")[0]),int(ass.split("-")[1])+1)),ass_pair))

    overlap = ass_sets[0].intersection(ass_sets[1])
    if (len(overlap) == min(list(map(lambda ass: len(ass), ass_sets)))):
        total_overlap_count += 1

    if (len(overlap) > 0):
        partial_overlap_count += 1


print(total_overlap_count)
print(partial_overlap_count)

