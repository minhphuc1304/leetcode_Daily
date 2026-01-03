class Solution:
    def numOfWays(self, n: int) -> int:
        n -= 1
        MOD = int(1e9 + 7)

        transition_matrix = [[3, 2],
                             [2, 2]]

        cur = [6, 6]
        while n:
            if n % 2 == 1:
                cur = [
                    (transition_matrix[0][0]*cur[0] + transition_matrix[0][1]*cur[1]) % MOD,
                    (transition_matrix[1][0]*cur[0] + transition_matrix[1][1]*cur[1]) % MOD
                ]
            n //= 2
            transition_matrix = [
                [
                    (transition_matrix[0][0]*transition_matrix[0][0] + transition_matrix[0][1]*transition_matrix[1][0]) % MOD,
                    (transition_matrix[0][0]*transition_matrix[0][1] + transition_matrix[0][1]*transition_matrix[1][1]) % MOD
                ],
                [
                    (transition_matrix[1][0]*transition_matrix[0][0] + transition_matrix[1][1]*transition_matrix[1][0]) % MOD,
                    (transition_matrix[1][0]*transition_matrix[0][1] + transition_matrix[1][1]*transition_matrix[1][1]) % MOD
                ]
            ]
    
        return (cur[0] + cur[1]) % MOD
