import sys
from itertools import groupby
def fasta_iter(fasta_name):
    fh = open(fasta_name)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        headerStr = header.__next__()[1:].strip().split()[0]#Entire line, add .split[0] for just first column
        seq = "".join(s.strip() for s in faiter.__next__())
        yield (headerStr, seq)
seq_length=0
with open("HLA_DQB1_subset.aa.mafft.phy", "w") as out:



    sequence_iterator = fasta_iter("HLA_DQB1_subset.aa.mafft.fasta")
    first_line =True
    for ff in sequence_iterator:

        headerStr, seq = ff
        if first_line:
            seq_length = len(seq)
            num_lines = num_lines = sum(1 for line in open("HLA_DQB1_subset.aa.mafft.trimal.fasta") if line[0]=='>')
            out.write(str(num_lines)+" "+str(seq_length)+"\n")
            first_line=False

        seq_length = len(seq)
        out.write(headerStr.strip('>')+"\t")
        out.write(seq +"\n")
