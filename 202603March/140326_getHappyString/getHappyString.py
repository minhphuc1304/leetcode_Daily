class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if 3 * 2 ** (n - 1) < k:
            return ""

        made, ans = 0, ''
        def backtrack(i, prev_letter):
            nonlocal made, ans
            if i == n - 1:
                made += 1

                if made == k:
                    return True
                return False

            letters = (s for s in 'abc' if s != prev_letter)
            for l in letters:
                if backtrack(i + 1, l):
                    ans += l
                    return True

            return False

        backtrack(-1, 'd')

        return ans[::-1]
