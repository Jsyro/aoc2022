import string

lines = [line.strip() for line in open("input.txt","r")]


total = 0
p2_total = 0

for num, sack in enumerate(lines): 
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


    ## PART 2
    if (num % 3 != 0):
        continue
    sack1 = sack
    sack2 = lines[num+1]
    sack3 = lines[num+2]

    items1 = set(sack1)
    items2 = set(sack2)
    items3 = set(sack3)

    shared_let = items1.intersection(items2).intersection(items3).pop()
    print (shared_let)


    sh_let_val = 1 
    if(shared_let.isupper()):
        sh_let_val+=26
        shared_let = shared_let.lower()
    sh_let_val += string.ascii_lowercase.index(shared_let)

    p2_total+=sh_let_val

print(total)
print(p2_total)