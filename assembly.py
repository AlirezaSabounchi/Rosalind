import time as t
begin = t.time()

def rev_comp(input) :
    dict, result = {"A":"T" , "T":"A" , "C":"G" , "G":"C"}, []
    for letter in reversed(input) :
        result.append(dict[letter])
    result = "".join(result)
    return result

def is_next(head, data, k) :
    for word in data :
        if word.startswith(head[k:]) :
            if data.index(word) > 1 :
                if data[data.index(word)-1] == rev_comp(word) :
                    del data[data.index(word)-1:data.index(word)+1]
                else :
                    del data[data.index(word):data.index(word)+2]
                return True, word, data
            elif data.index(word) == 0 or data.index(word) == 1  :
                del data[0:2]
                return True, word, data
    return False, [], data

def construct(list, k) :
    result = []
    result.append(list[0])
    for i in list[1:] :
        result.append(i[k:])
    return "".join(result)


with open("rosalind_gasm.txt") as file :
    text = file.read().split("\n")
data = []
for line in text :
    data.append(line)
    data.append(rev_comp(line))

temp, string = [], []
for k in range(1,len(data[0])-1) :
    start = data[0]
    new_data = data
    while 1 :
        next_found, next, new_data = is_next(start, new_data, k)
        if next_found and next != []:
            string.append(next)
            start = next
            continue
        elif next_found != True or new_data == [] :
            break
    #print(len(new_data))
    if len(new_data) <= 2* (len(data[0]) // k) :
        #ignore = len(data[0]) // k
        #print(string)
        #for i in range(ignore-1):
        #    del string[-1]
        print(string)
        temp = construct(string, len(data[0])-k)
        break
    string = []

ending = t.time()
#print(temp)

#-ignore*(len(data[0])-k)
print(construct(max(string, key=len)))
print(construct(string[string.index(max(string, key=len))]))
