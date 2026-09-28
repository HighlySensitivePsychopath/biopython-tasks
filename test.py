from Bio import SeqIO

# 1. Wczytujemy pobrany plik FASTA
for record in SeqIO.parse("sequence.fasta", "fasta"):
    print("=" * 50)
    print(f"🧬 NAZWA GENU: {record.description}")
    print(f"📏 DŁUGOŚĆ: {len(record.seq)} liter (zasad azotowych)")
    print("=" * 50)
    
    # Przypisujemy sekwencję do zmiennej dla wygody
    dna = record.seq
    
    # 2. LICZENIE STATYSTYK: Ile mamy poszczególnych liter?
    count_A = dna.count("A")
    count_T = dna.count("T")
    count_G = dna.count("G")
    count_C = dna.count("C")
    
    print("\n[1] Analiza składu chemicznego:")
    print(f" Adenina (A): {count_A}")
    print(f" Tymina (T):  {count_T}")
    print(f" Guanina (G): {count_G}")
    print(f" Cytozyna (C): {count_C}")
    
    # 3. OBLICZANIE WSPÓŁCZYNNIKA GC (GC-Content)
    # To procentowy udział silniejszych wiązań (G i C) w całym genie
    gc_content = (count_G + count_C) / len(dna) * 100
    print(f"\n📊 Współczynnik GC: {gc_content:.2f}%")
    
    if gc_content > 50:
        print(" -> Ten gen ma wysoką stabilność termiczną (więcej par G-C).")
    else:
        print(" -> Ten gen ma standardową stabilność termiczną (więcej par A-T).")
        
    # 4. TRANSLACJA: Zobaczmy początek białka, które ten gen tworzy
    # Ignorujemy ewentualne błędy długości (niepodzielność przez 3) za pomocą cds=False lub domyślnego translate
    protein = dna.translate()
    print(f"\n[2] Pierwsze 15 aminokwasów powstałego białka:")
    print(f" 🧪 {protein[:15]}...")
    print("=" * 50)
