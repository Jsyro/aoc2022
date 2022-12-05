import string

lines = [line.strip() for line in open("input.txt","r")]


total = 0
for sack in lines: 
    compL = sack[:int(len(sack)/2)]
    compR = sack[int(len(sack)/2):]

    dup_let = set(compR).intersection(set(compL)).pop()
    let_val = 1 
    if(dup_let.isupper()):
        let_val+=26
        dup_let = dup_let.lower()
    let_val += string.ascii_lowercase.index(dup_let)

    print(dup_let)
    print(let_val)
    total += let_val

print(total)