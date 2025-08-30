class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return not any(x in s or s.add(x) for s in [set()] for i,row in enumerate(board) for j,v in enumerate(row) for x in ((v,'r',i),(v,'c',j),(v,'b',i//3,j//3)) if v!='.')
