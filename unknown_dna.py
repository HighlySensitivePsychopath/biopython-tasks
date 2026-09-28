from Bio import SeqIO


max=0
id_max=None
# 1. Wczytujemy pobrany plik FASTA
for record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    
    dna = record.seq

    count_A = dna.count("A")
    count_T = dna.count("T")
    count_G = dna.count("G")
    count_C = dna.count("C")

    gc_content = (count_G + count_C) / len(dna) * 100
    if gc_content>max:
        max=gc_content
        id_max=record.description
        
 
print(id_max)
print(max)
