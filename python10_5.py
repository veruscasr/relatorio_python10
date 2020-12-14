#!/usr/bin/end python3

#$ -q all.q
#$ -cwd
#$ -V
#$ -pe smp 1
##$ -l h=bcmserv

#INPUT
dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

#def count_dna(dna, n): ## give our function a name and parameter 'dna'
#        dna_list = []  #lista
#        for i in range(0, len(dna), n):
#                nucleotides = dna[i:i+n]
#                dna_list.append(nucleotides)
#        for i in dna_list:
#                print(i)

#print(count_dna(dna, 60))

def gc_content(dna):   # give our function a name and parameter 'dna'
   c_count = dna.count('C')
   g_count = dna.count('G')
   print(c_count, g_count)   

   dna_len = len(dna)
   print(dna_len)

   gc_content = (c_count + g_count) / dna_len
   return gc_content

print(gc_content(dna)) # return the value to the code that called this function
