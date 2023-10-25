from Bio.Seq import Seq

# Criando uma sequência de nucleotídeos (DNA) com comprimento múltiplo de três
dna_sequence = Seq("ATGCGAAGCTCTTACCAGCTAGGA")

# Imprimindo a sequência de DNA
print("Sequência de DNA:", dna_sequence)

# Obtendo a sequência complementar
complement_sequence = dna_sequence.complement()
print("Complemento da sequência de DNA:", complement_sequence)

# Obtendo a sequência reversa complementar
reverse_complement_sequence = dna_sequence.reverse_complement()
print("Reverso complementar da sequência de DNA:", reverse_complement_sequence)

# Obtendo a transcrição para RNA
rna_sequence = dna_sequence.transcribe()
print("Sequência de RNA:", rna_sequence)

# Obtendo a tradução para proteína
protein_sequence = dna_sequence.translate()
print("Sequência de Proteína:", protein_sequence)
