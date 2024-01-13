with open("rosalind_asmq.txt") as file :
    text = file.read().split("\n")

def assess(text, threshold) :
    all = sum([len(line) for line in text])
    for L in range(len(max(text, key=len))-1 , 0 , -1) :
        summ = 0
        for string in text :
            if len(string) >= L :
                summ += len(string)
        if float(summ/all) >= threshold :
            return L
print(assess(text, 0.5), assess(text, 0.75), sep = " ")
