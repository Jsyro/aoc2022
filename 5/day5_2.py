from typing import List

lines = [line for line in open("input.txt","r")]

cargo_init = lines[:9]
move_list = lines[10:]

cargo: List[List[str]] = [[] for n in range(0,9)]


for cargo_line in cargo_init[-2::-1]:
    crates = [cargo_line[col].strip() for col in range(1,9*4,4)]
    for col, crate in enumerate(crates):
        if crate:
            cargo[col].append(crate)
    
print(cargo)

for move in move_list:
    num_move = int(move.split(" ")[1])
    from_stack = int(move.split(" ")[3])-1
    to_stack = int(move.split(" ")[5])-1

    src_stack=cargo[from_stack][:] #make a copy
    cargo[from_stack] = src_stack[:-num_move] #remove crates to be moved
    moving_stack = src_stack[-num_move:] #crates to be moved
    cargo[to_stack]+=moving_stack #put crates down. 


print(''.join([stack.pop() for stack in cargo]))
