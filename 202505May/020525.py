class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left = [float('inf')] * n
        right = [float('inf')] * n

        # Tính lực từ bên phải (R) sang trái
        time = float('inf')
        for i in range(n):
            if dominoes[i] == 'R':
                time = 0
            elif dominoes[i] == 'L':
                time = float('inf')
            else:
                if time != float('inf'):
                    time += 1
            right[i] = time

        # Tính lực từ bên trái (L) sang phải
        time = float('inf')
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                time = 0
            elif dominoes[i] == 'R':
                time = float('inf')
            else:
                if time != float('inf'):
                    time += 1
            left[i] = time

        # So sánh và kết luận
        result = []
        for l, r in zip(left, right):
            if l == r:
                result.append('.')
            elif l < r:
                result.append('L')
            else:
                result.append('R')

        return ''.join(result)
