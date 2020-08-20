def rectangles(strings):
    if len(strings) < 2:
        return 0
    matrix = [list(row) for row in strings]
    length = len(matrix[0])
    height = len(matrix)
    rects = 0

    def is_hor_conn(left, right, row):
        for col in matrix[row][left+1:right]:
            if col == ' ' or col == '|':
                return False
        return True
    
    def is_ver_conn(top, bottom, col):
        col_l = [matrix[row][col] for row in range(top+1,bottom)]
        for c in col_l:
            if c == ' ' or c == '-':
                return False
        return True

    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if col == '+':
                for right in range(x+1, length):
                    if matrix[y][right] == '+' and is_hor_conn(x,right,y):
                        for bottom in range(y+1, height):
                            if  ( matrix[bottom][x] == '+'
                                and matrix[bottom][right] == '+'
                                and is_ver_conn(y,bottom,x)
                                and is_ver_conn(y,bottom,right)
                                and is_hor_conn(x,right, bottom)):
                                #print(f"left:{x} right:{right} top:{y} bottom{bottom}")
                                rects += 1
    
    return rects
