class Solution:
    def factorial(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def generate_k_palindromes(self, current, index, k_palindromes, k):
        if index >= (len(current) + 1) // 2:
            if int(current) % k == 0:
                k_palindromes.append(current)
            return

        if index != 0:
            temp = current
            temp = temp[:index] + '0' + temp[index+1:]
            temp = temp[:len(temp) - index - 1] + '0' + temp[len(temp) - index:]
            self.generate_k_palindromes(temp, index + 1, k_palindromes, k)

        for digit in range(1, 10):
            temp = current
            temp = temp[:index] + str(digit) + temp[index+1:]
            temp = temp[:len(temp) - index - 1] + str(digit) + temp[len(temp) - index:]
            self.generate_k_palindromes(temp, index + 1, k_palindromes, k)

    def countGoodIntegers(self, n, k):
        k_palindromes = []
        initial_form = "0" * n
        self.generate_k_palindromes(initial_form, 0, k_palindromes, k)

        digit_patterns = set()

        for palindrome in k_palindromes:
            freq = ['0'] * 10
            for digit in palindrome:
                idx = int(digit)
                if freq[idx] == '9':
                    freq[idx] = 'A'  # đại diện cho > 9 lần xuất hiện
                elif freq[idx] == 'A':
                    continue
                else:
                    freq[idx] = str(int(freq[idx]) + 1)
            digit_patterns.add(''.join(freq))

        total_permutations = self.factorial(n)
        total_count = 0

        for pattern in digit_patterns:
            permutations = total_permutations
            for freq in pattern:
                count = 10 if freq == 'A' else int(freq)
                permutations //= self.factorial(count)

            if pattern[0] != '0':  # nếu có chữ số 0 → cần trừ các số bắt đầu bằng 0
                leading_zero_count = int(pattern[0]) - 1
                permutations_with_leading_zero = self.factorial(n - 1)

                for freq in pattern[1:]:
                    count = 10 if freq == 'A' else int(freq)
                    permutations_with_leading_zero //= self.factorial(count)
                permutations_with_leading_zero //= self.factorial(leading_zero_count)

                permutations -= permutations_with_leading_zero

            total_count += permutations

        return total_count
