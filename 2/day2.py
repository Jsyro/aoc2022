
lines = [line.strip() for line in open("input.txt","r")]

print(lines[:20])

r_val = "A","X"
p_val = "B","Y"
s_val = "C","Z"

#self, round_score, beats,losses

r = "r",1,"s","p"
p = "p",2,"r","s"
s = "s",3,"p","r"

def parse_move(letter:str):
    #score my_move
    move = None
    if letter in r_val:
        move = r
    if letter in p_val:
        move = p
    if letter in s_val:
        move = s
    return move

total_score = 0
round_scores = []

for round in lines: 
    round_score = 0

    op_let,my_let = round.split()

    op_move = parse_move(op_let)
    my_move = parse_move(my_let)
    
    round_score += my_move[1]
   
    #tie
    if my_move[0] == op_move[0]:
        round_score += 3

    #win
    if my_move[0] == op_move[3]:
        round_score += 6

    total_score += round_score
    round_scores.append(round_score)

print(len(round_scores))
print(total_score)