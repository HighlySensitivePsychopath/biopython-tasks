f = open("rosalind_dna.txt")
file = f.read().strip()

#print(len(file))
print(file.count("A"), file.count("C"), file.count("G"), file.count("T"))