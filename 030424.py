# https://leetcode.com/problems/word-search/solutions/

# 79. Word Search

def exist(board, word):
        
    def neighbours(i, j):
        for d in (-1, 1):
            if 0 <= i+d < len(board):
                yield i+d, j, board[i+d][j]
            if 0 <= j+d < len(board[0]):
                yield i, j+d, board[i][j+d] 

    def dfs(idx, i, j):
        visited[i][j] = True
        if idx == 0:
            return board[i][j] == word[0]
        next_char = word[idx-1]            
        for ni, nj, nch in neighbours(i, j):
            if next_char == nch and not visited[ni][nj] and dfs(idx-1, ni, nj):
                return True
        visited[i][j] = False 
        return False

    for i, row in enumerate(board):
        for j, ch in enumerate(row): 
            if ch == word[-1]: 
                visited = [[False] * len(board[0]) for _ in board]
                if dfs(len(word)-1, i, j):
                    return True
    return False
        

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(exist(board, word))

            
        