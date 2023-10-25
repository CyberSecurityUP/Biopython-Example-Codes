# Manipulação básica de sequências
from Bio.Seq import Seq

# Declarando uma sequência
seq1 = Seq("ACGTAGCTACGATCACAGCTA")
print("Minha sequência é", seq1)

# Reverso complementar
rc = seq1.reverse_complement()
print("O reverso complementar é", rc)

# Transcrição
rna = seq1.transcribe()
print("A sequência transcrita é", rna)

# Tradução
protein = seq1.translate()
print("A sequência da proteína é", protein)

