dict = {"A":4 , "R":6 , "N":2 , "D":2 , "C":2 , "E":2 , "Q":2 , "G":4 , "H":2 , "I":3 , "L":6 , "K":2 , "M":1 , "F":2 , "P":4 , "S":6 , "T":4 , "W":1 , "Y":2 , "V":4 }
string, res = [], 3

with open("rosalind_mrna.txt") as file :
    protein = file.read().replace("\n", "")
for aa in protein :
    res *= dict[aa]
print(res%1000000)
