class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # cols = defaultdict(set) #init colums
        # row = defaultdict(set)  # init rows
        # square = defaultdict(set)   #r//3 c//3

        # for r in range (9):
        #     for c in range (9):
        #         if board [r][c] == ".":  #empty
        #             continue # skip 
        #         if (
        #             board[r][c] in row[r]
        #             or board[r][c] in cols[c]
        #             or board[r][c] in square [(r //3 , c//3)]
        #         ):
        #             return False
        #         cols[c].add(board[r][c])
        #         row[r].add(board[r][c])
        #         square[(r//3 , c//3)]. add(board[r][c])
        # return True
        colus = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)

        for r in range (9):
            for c in range (9):
                if board [r][c] == ".":
                    continue 
                if (
                    board[r][c] in rows[r]
                    or board [r][c] in colus[c]
                    or board [r][c] in square [(r//3, c//3)]
                ):
                    return False
                colus[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3 ,c//3)].add(board[r][c])
        return True



            
        