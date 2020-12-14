#!/usr/bin/env python3

import sys

dna_seq_fasta = sys.argv[0]
#max_len = int(sys.argv[1])
#open = '/Storage/data1/verusca.rossi/Aula_programacao/dna_seq_python10.fasta'

def count_dna(dna_seq_fasta, n):
	dna_list = []  
	for i in range(0, len(dna_seq_fasta), n):
		nucleotides = dna_seq_fasta[i:i+n]
		dna_list.append(nucleotides)
	for i in dna_list:
		print(i)

print(count_dna(dna_seq_fasta, 60))

#max_lenght = int(sys.argv[1])

#if max_lenght > len(dna_list):
#	print("Max lenght is 60")

	






	#else:
        #print('Max line lenght is 60')

