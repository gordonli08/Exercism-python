def saddle_points(matrix):
    #case for empty matrix
    if not matrix:
    	return []

    #case for irregular matrix
    rowlen = len(matrix[0])
    for row in matrix:
    	if len(row) != rowlen:
    		raise ValueError('Irregular matrix submitted')

    #case for finding points in acceptable matrix
    highrow = [sorted(row, reverse=True)[0] for row in matrix]
    lowcol = [sorted(col)[0] for col in ((row[c] for row in matrix) for c in range(len(matrix[0])))]
    points = []

    for rownum, row in enumerate(matrix):
    	for i,v in enumerate(row):
    		if v >= highrow[rownum] and v <= lowcol[i]:
    			points.append(
    				{
    					"row": rownum + 1,
    					"column": i + 1
    				
    				})

    return points
