f = open("rosalind_revc.txt")
file = f.read().strip()
#print (file)

file = file [::-1]

char={"A":"T","T":"A","C":"G","G":"C"}

print(''.join(char.get(s, s) for s in file))
