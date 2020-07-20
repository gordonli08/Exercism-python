WHITE = 'W'
BLACK = 'B'
NONE = ' '

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = [list(row) for row in board]
        self.row_len = len(board[0])
        self.col_len = len(board)



    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """

        if not (0 <= x < self.row_len and 0 <= y < self.col_len):
            raise ValueError('X or Y is out of bounds')

        if not self.board[y][x] == NONE:
            return (NONE, set())

        terr_set = set()
        visit_q = [(x, y)]
        visited = set()
        owner = set()

        while visit_q:
            curr = visit_q.pop(0)
            visited.add(curr)
            if self.board[curr[1]][curr[0]] == NONE:
                terr_set.add(curr)
                
                if 0 <= curr[0] - 1 and (curr[0] - 1, curr[1]) not in visited:
                    visit_q.append((curr[0] - 1, curr[1]))
                    owner.add(self.board[curr[1]][curr[0]-1])
                
                if curr[0] + 1 < self.row_len and (curr[0] + 1, curr[1]) not in visited:
                    visit_q.append((curr[0] + 1, curr[1]))
                    owner.add(self.board[curr[1]][curr[0]+1])

                if 0 <= curr[1] - 1 and (curr[0], curr[1] - 1) not in visited:
                    visit_q.append((curr[0], curr[1] - 1))
                    owner.add(self.board[curr[1]-1][curr[0]])

                if curr[1] + 1 < self.col_len and (curr[0], curr[1] + 1) not in visited:
                    visit_q.append((curr[0], curr[1] + 1))
                    owner.add(self.board[curr[1]+1][curr[0]])
        """
        print terr_set
        print visit_q
        print visited
        print owner
        """
        stone = NONE
        if BLACK in owner and WHITE not in owner:
            stone = BLACK
        elif WHITE in owner and BLACK not in owner:
            stone = WHITE

        return stone, terr_set




    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        terr_dict = {
            BLACK: set(),
            WHITE: set(),
            NONE: set()
        }

        visit_q = set((x,y) for x in range(0, self.row_len) for y in range(0, self.col_len))

        while visit_q:
            curr = visit_q.pop()
            if self.board[curr[1]][curr[0]] == NONE:
                stone, terr = self.territory(curr[0],curr[1])
                terr_dict[stone] |= terr
                visit_q = visit_q - terr

        return terr_dict

"""
board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
stone, territory = board.territory(x=2, y=3)
print stone
print territory

board2 = Board([" "])
territories = board2.territories()
"""
