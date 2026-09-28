f = open("rosalind_rna.txt")
file = f.read().strip()

ans = file.replace("T", "U")

print(ans)