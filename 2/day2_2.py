
lines = [line.strip() for line in open("input.txt","r")]

print(lines[:20])

r_val = "A"
p_val = "B"
s_val = "C"


#self, round_score, beats,losses

r = "r",1,"s","p"
p = "p",2,"r","s"
s = "s",3,"p","r"


#op_move, round_score, x,y,z
#x  lose
#y draw
#z= win 
r_2 = {"let":r_val, "self": "r","score":1,"X":s,"Y":r,"Z":p}
p_2 = {"let":p_val, "self": "p","score":2,"X":r,"Y":p,"Z":s}
s_2 = {"let":s_val, "self": "s","score":3,"X":p,"Y":s,"Z":r}

debug=0

def parse_move(letter:str):
    #score my_move
    move = None
    if letter in r_val:
        move = r_2
    if letter in p_val:
        move = p_2
    if letter in s_val:
        move = s_2
    return move

total_score = 0
round_scores = []

for round in lines: 
    round_score = 0

    op_let,my_let = round.split()
    if debug:
        print(op_let)
        print(my_let)

    op_move = parse_move(op_let)
    #tie
    if my_let == "Y":
        round_score += 3

    #win
    if my_let == "Z":
        round_score += 6
    if debug:
        print(op_move)
        print(op_move[my_let][1])

    let_score = op_move[my_let][1]

    if debug:
        print(round_score)
        print(let_score)
        print()

    total_score += round_score + let_score
    round_scores.append(round_score)

print(len(round_scores))
print(total_score)