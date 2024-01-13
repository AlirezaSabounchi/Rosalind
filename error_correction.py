def rev_comp(input) :
    dict, result = {"A":"T" , "T":"A" , "C":"G" , "G":"C"}, []
    for letter in reversed(input) :
        result.append(dict[letter])
    result = "".join(result)
    return result


def hamming(input1, input2) :
    count = 0
    for letter in range(len(input1)) :
        if input1[letter] != input2[letter] :
            count += 1
    return count


def correction(input, database) :
    for row in database :
        if hamming(input, row) == 1 :
            return [input , row]
        elif hamming(rev_comp(input), row) == 1 :
            return [input , rev_comp(row)]

data = []
with open("rosalind_corr.txt") as file :
    text = file.read().replace("\n", "").split(">")
for line in text :
    data.append(line[13:]) ###############
del data[0]

for each in data :
    if data.count(each) < 2 and data.count(rev_comp(each)) < 1 :
        res = correction(each, data)
        data[data.index(each)] = res[1]
        print(res[0], "->", "".join(res[1]), sep = "")
