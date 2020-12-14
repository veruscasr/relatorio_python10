#!/usr/bin/env python3


class DNARecord(object):
# define class attributes
	sequence = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
#	species_name = 'Pan troglodytes'
#	gene_name = 'TP53'
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

# define methods
#def reverse_complement(self):
#	replacement1 = self.sequence.replace('A', 't')
#	replacement2 = replacement1.replace('T', 'a')
#	replacement3 = replacement2.replace('C', 'g')
#	replacement4 = replacement3.replace('G', 'c')
#	reverse_comp = replacement4[::-1]
#	return reverse_comp.upper()

#print(reverse_complement)

def complement_base(base):
     
	if base in 'Aa':
		return 'T'
	elif base in 'Tt':
		return 'A'
	elif base in 'Gg':
		return 'C'
	else:
		return 'G'

def reverse_complement(sequence):
    """Compute reverse complement of a sequence."""
    
    # Initialize reverse complement
    rev_sequence = ''
    
    # Loop through and populate list with reverse complement
    for base in reversed(sequence):
        rev_sequence += complement_base(base)
        
    return rev_sequence

print(reverse_complement)









