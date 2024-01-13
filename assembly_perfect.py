def rev_comp(input) :
    dict, result = {"A":"T" , "T":"A" , "C":"G" , "G":"C"}, []
    for letter in reversed(input) :
        result.append(dict[letter])
    result = "".join(result)
    return result

def is_next(head, data) :
    for word in data :
        if word.startswith(head[1:]) :
            return True, word
    return False, []

def construct(list) :
    result = []
    result.append(list[0])
    for i in list[1:] :
        result.append(i[-1])
    return "".join(result)


with open("temp.txt") as file :
    text = file.read().split("\n")
data = set()
for line in text :
    data.add(line)
    data.add(rev_comp(line))

heads, string = [], []
heads.extend(data)

start = heads[0]
while 1 :
    next_found, next = is_next(start, heads)
    if next_found and next not in string:
        string.append(next)
        start = next
        continue
    else :
        break

print(construct(string)[:-49])
