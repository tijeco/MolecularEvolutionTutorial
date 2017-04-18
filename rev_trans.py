import sys
from itertools import groupby
def fasta_iter(fasta_name):
    fh = open(fasta_name)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        headerStr = header.__next__()[1:].strip().split()[0]#Entire line, add .split[0] for just first column
        seq = "".join(s.strip() for s in faiter.__next__())
        yield (headerStr, seq)
cut = ""

longIsoform_CDS_combined = {}

sequence_iterator = fasta_iter(sys.argv[1])
		#sample = input.cds_before[currentFile].split('.')[0]
for ff in sequence_iterator:

		headerStr, seq = ff
		GeneID = headerStr

		if GeneID not in longIsoform_CDS_combined:
						longIsoform_CDS_combined[GeneID] = seq
#Open outout
print(len(longIsoform_CDS_combined))
#print(longIsoform_CDS_combined)

with open(sys.argv[4], "w") as out:


		#Get  column cut file
		with open(sys.argv[2]) as f:
				for line in f:
						cut  +=line.strip()
				cut = cut.split(',')
				cut = list(map(int, cut))
		print(cut)

		#Get corresponding untrimmed Alignments, as original, line by line
		line1=True
		first_line=True
		with open(sys.argv[3]) as f:
				for line in f:
						if line1:

								line1=False
								continue

						row =line.strip().split()
						# print("***********")
						# print(row)
						# print("____________")
						original=row[1]#cds
						header=row[0]
						#print("Sequence:",sequence)
						#print("Header:",header)
						try:
								sequence=longIsoform_CDS_combined[header]#original
						except:
								print(header,"not in dict")
						#print(sequence)
						CodonPos={}
						position=0
						codon=""
						number=1
						for i in sequence:

								codon +=i
								#print i,position%3,codon
								if position%3==2:
										#print codon
										#print codonTable[codon]
										CodonPos[number]=codon
										number+=1
										#protein+=codonTable[codon]
								position +=1

								if position%3==0:
										#print codon
										codon=""
						#print(CodonPos)
						aaPos=0
						firstAA=True
						alnPos=0
						prot=""
						trimmed=""
						for i in original:
								if i!="-":
										aaPos+=1

								if alnPos in cut:
										prot+=i
										if i != "-":
												trimmed+=CodonPos[aaPos]
										else:
												trimmed+="---"
								alnPos+=1
						num_lines = sum(1 for line in open(sys.argv[3]) )
						if first_line:
								out.write(str(num_lines-1) + " " + str(len(trimmed)) + '\n')
								first_line=False
						out.write(header+'   '+trimmed+'\n')
						print(trimmed,None)
