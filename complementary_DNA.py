"""https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python"""

DNA_MAP = {"A": "T", "T": "A", "G": "C", "C": "G"}

def DNA_strand(dna):
    return ''.join(map(lambda x: DNA_MAP[x], dna))


DNA_MAP = {"A": "T", "T": "A", "G": "C", "C": "G"}

def DNA_strand2(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

print(DNA_strand2("ATTGC"))
