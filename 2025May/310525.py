class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = deque([(1, 0)])
        visited = [False] * (n * n + 1)
        visited[1] = True
        
        def flattenBoard() -> List[int]:
            flattened = [-1] * (n * n + 1)
            idx = 1
            
            for row in range(n - 1, -1, -1):
                leftToRight = ((n - 1 - row) % 2 == 0)
                
                if leftToRight:
                    for col in range(0, n):
                        if board[row][col] != -1:
                            flattened[idx] = board[row][col]
                        idx += 1
                else:
                    for col in range(n - 1, -1, -1):
                        if board[row][col] != -1:
                            flattened[idx] = board[row][col]
                        idx += 1
        
            return flattened        
        
        
        flattened = flattenBoard()
        
        while queue:
            position, moves = queue.popleft()
            if position == n * n:
                return moves
            
            for dice in range(1, 7):
                nextPosition = position + dice
                if nextPosition > n * n:
                    break
                
                if flattened[nextPosition] != -1:
                    nextPosition = flattened[nextPosition]
                
                if not visited[nextPosition]:
                    visited[nextPosition] = True
                    queue.append((nextPosition, moves + 1))
        
        return -1        
