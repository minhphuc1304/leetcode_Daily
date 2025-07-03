# Happy birthday to My love
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        ans: int = 0
        count: int = 0
        
        j: int = 1
        while True:
            for i in self.magic_function_to_get_base_10_mirror_numbers(length=j):
                if self.magic_function_to_check_if_palindrome_in_base_k(k, i):
                    ans += i
                    count += 1
                    if count == n:
                        return ans
            j += 1
    
    def magic_function_to_get_base_10_mirror_numbers(self, length: int) -> Iterator[int]:
        # Simple case length = 1
        if length == 1:
            for i in range(1, 10):
                yield i
            return
        
        # If the length is not 1
        # The first digit can be whatever between 1 and 9. From the second digit to length//2 (length//2 not included),
        # we can have anything between 0 and 9.
        # If length % 2 == 1, the digit at index length//2 can be whatever.
        # From length//2 + 1 to the end, we have no choice but follow the first half.
        num_digits: list[int] = [0] * length
        num_digits[0] = 1
        num_digits[-1] = 1
        yield from self.magic_function_to_transform_num_digits(length, num_digits)
        ptr: int = length//2 - 1
        while True:
            if num_digits[ptr] != 9:
                num_digits[ptr] += 1
                num_digits[length - 1 - ptr] += 1
                yield from self.magic_function_to_transform_num_digits(length, num_digits)
            else:
                while num_digits[ptr] == 9 and ptr >= 0:
                    num_digits[ptr] = 0
                    num_digits[length - 1 - ptr] = 0
                    ptr -= 1
                if ptr == -1:
                    return
                num_digits[ptr] += 1
                num_digits[length - 1 - ptr] += 1
                for integer in self.magic_function_to_transform_num_digits(length, num_digits):
                    yield integer
                ptr = length//2 - 1

    def magic_function_to_transform_num_digits(self, length: int, num_digits: list[int]):
        if length % 2 == 0:
            yield int(''.join(map(str, num_digits)))
        else:
            for k in range(10):
                num_digits[length//2] = k
                yield int(''.join(map(str, num_digits)))
    
    def magic_function_to_check_if_palindrome_in_base_k(self, k: int, i: int) -> bool:
        # Convert i in base k
        num_digits: list[int] = []
        while i > 0:
            num_digits.append(i % k)
            i //= k
        return num_digits == num_digits[::-1]
