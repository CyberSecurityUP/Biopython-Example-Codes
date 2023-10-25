from Bio import ExPASy
from Bio import SwissProt

# ID da glicoproteína no UniProt
protein_id = "Q0P9C4"

# Baixa informações da proteína do UniProt
handle = ExPASy.get_sprot_raw(protein_id)
record = SwissProt.read(handle)

# Exibe informações sobre a proteína
print("ID:", record.entry_name)
print("Nome:", record.description)
print("Organismo:", record.organism)
print("Sequência de aminoácidos:", record.sequence)

# Verifica se a proteína tem informações sobre glicosilação
if 'Glycosylation' in record.cross_references:
    glycosylation_info = [x[2] for x in record.cross_references['Glycosylation']]
    print("Informações sobre glicosilação:", glycosylation_info)
else:
    print("Esta proteína não possui informações sobre glicosilação no UniProt.")
