def to_rna(dna_strand):
    rna_dict = {
    	'C':'G',
    	'G':'C',
    	'T':'A',
    	'A':'U'
    }
    ret = ''

    for char in dna_strand:
    	ret += rna_dict[char]

    return ret

