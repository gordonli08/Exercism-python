neighbours = [(-1,0), (1,0), (0,-1), (1,-1), (-1,1), (0,1)]
class ConnectGame:
    def __init__(self, board):
        self.o_board =  [row.strip().split() for row in board.splitlines()]
        self.x_board = list(map(list, zip(*self.o_board)))
        """
        print(f"{self.row_len}, {self.col_len}")
        print('o board')
        print(self.o_board)
        print('x board')
        print(self.x_board)
        """

    def get_winner(self):
        for player in ['O','X']:
            result = self.checkwinner(player)
            if result:
                return player
        return ''

    def checkwinner(self, player):
        if player == 'X':
            board = self.x_board
            row_len = len(self.x_board[0])
            col_len = len(self.x_board)
        else:
            board = self.o_board
            row_len = len(self.x_board[0])
            col_len = len(self.o_board)
        #print(board)
        starts = [(x, 0) for x, stone in enumerate(board[0]) if stone == player]
        while starts:
            top = starts.pop(0)
            visited = set()
            visit_q = [top]
            route = set()
            #explore
            while visit_q:
                curr = visit_q.pop(0)
                visited.add(curr)
                #print(f"{curr[0]}, {curr[1]}")
                if board[curr[1]][curr[0]] == player:
                    if curr[1] == col_len - 1:
                        return True
                    route.add(curr)
                    if curr in starts:
                        starts.remove(curr)
                for neighbour in neighbours:
                    row = curr[0]+neighbour[0]
                    col = curr[1]+neighbour[1]
                    if row < 0 or col < 0:
                        continue
                    try:
                        if board[col][row] == player and (row,col) not in visited:
                            #print(f"{row}, {col} {board[col][row]} hit")
                            visit_q.append((row,col))
                    except IndexError:
                        continue
                #print(visit_q)
            return False

