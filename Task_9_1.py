# Первая задача к девятому занятию
dna = list(input())
rna = []

dna_to_rna = {
    "G": "C", 
    "C": "G", 
    "T": "A", 
    "A": "T"
}

for letter in dna:
    for k, v in dna_to_rna.items():
        if letter == k:
            rna.append(v)
print("".join(rna))
