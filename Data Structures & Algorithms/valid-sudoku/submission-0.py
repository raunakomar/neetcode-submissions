class Solution:
    def isSquareValid(self,board:List[List[str]],start_row,start_col)->bool:
        map = {}
        for r in range(0,3):
            for c in range(0,3):
                if (board[start_row+r][start_col+c]!='.' and board[start_row+r][start_col+c]) in map:
                    return False
                else:
                    map[board[start_row+r][start_col+c]] = 1
        return True
        
    def isRowValid(self,board:List[List[str]],row)->bool:
        map = {}
        for col in range(0,9):
            if (board[row][col]!='.' and board[row][col]) in map:
                return False
            else:
                map[board[row][col]] = 1
        return True
    def isColumnValid(self,board:List[List[str]],col)->bool:
        map = {}
        for row in range(0,9):
            if (board[row][col]!='.' and board[row][col]) in map:
                return False
            else:
                map[board[row][col]] = 1
        return True
    def areRowsValid(self,board:List[List[str]])->bool:
        for i in range(0,9):
            if(self.isRowValid(board,i)==False):
                return False
        return True
    def areColsValid(self,board:List[List[str]])->bool:
        for i in range(0,9):
            if(self.isColumnValid(board,i)==False):
                return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if(self.isSquareValid(board,0,0) == False):
            print(0,0)
            return False
        if(self.isSquareValid(board,0,3) == False):
            return False
        if(self.isSquareValid(board,0,6) == False):
            return False
        if(self.isSquareValid(board,3,0) == False):
            return False
        if(self.isSquareValid(board,3,3) == False):
            return False
        if(self.isSquareValid(board,3,6) == False):
            return False
        if(self.isSquareValid(board,6,0) == False):
            return False
        if(self.isSquareValid(board,6,3) == False):
            return False
        if(self.isSquareValid(board,6,6) == False):
            return False
        if(self.areRowsValid(board) == False):
            return False
        if(self.areColsValid(board) == False):
            return False
        return True
        
        