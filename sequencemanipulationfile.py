from Bio import SeqIO
from Bio.Seq import MutableSeq

def process_sequence(record):
    # Verificar se a sequência não é None e não está vazia
    if record.seq is not None and len(record.seq) > 0:
        # Exibir informações do registro
        print(f"ID: {record.id}")
        print(f"Descrição: {record.description}")
        print(f"Sequência original: {record.seq}")

        # Modificar a sequência (por exemplo, substituir A por T)
        modified_seq = MutableSeq(str(record.seq))
        modified_seq[0] = "T"  # Substituir o primeiro nucleotídeo por T
        record.seq = str(modified_seq)

        print(f"Sequência modificada: {record.seq}\n")
    else:
        print(f"SeqRecord (id={record.id}) tem uma sequência inválida ou vazia e será ignorado.")

# Caminho para o arquivo de sequência (substitua pelo caminho correto)
file_path = "sequences.fasta"

# Lista para armazenar os registros modificados
modified_records = []

# Iterar sobre os registros
with open(file_path, "r") as file:
    for record in SeqIO.parse(file, "fasta"):
        process_sequence(record)
        # Adicionar à lista apenas se a sequência for válida
        if record.seq is not None and len(record.seq) > 0:
            modified_records.append(record)

# Salvar os registros modificados em um novo arquivo (substitua pelo caminho correto)
output_file_path = "sequences_modificado.fasta"
with open(output_file_path, "w") as output_file:
    SeqIO.write(modified_records, output_file, "fasta")

print(f"Registros modificados foram salvos em: {output_file_path}")
