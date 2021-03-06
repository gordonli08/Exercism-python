def proteins(strand):
	proteinDict = {
		'AUG':'Methionine',
		'UUU':'Phenylalanine',
		'UUC':'Phenylalanine',
		'UUA':'Leucine',
		'UUG':'Leucine',
		'UCU':'Serine',
		'UCC':'Serine',
		'UCA':'Serine',
		'UCG':'Serine',
		'UAU':'Tyrosine',
		'UAC':'Tyrosine',
		'UGU':'Cysteine',
		'UGC':'Cysteine',
		'UGG':'Tryptophan',
		'UAA':'STOP',
		'UAG':'STOP',
		'UGA':'STOP'
	}

	strandlist = [strand[i:i+3] for i in range(0, len(strand), 3)]

	ret = []
	for seq in strandlist:
		if proteinDict[seq] == 'STOP':
			break
		ret.append(proteinDict[seq])

	return ret

