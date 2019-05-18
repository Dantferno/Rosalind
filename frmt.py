from Bio import Entrez
from Bio import SeqIO
Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
print records[0].id  #first record id
gi|227437129|gb|FJ817486.1|
print len(records[-1].seq)
