class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3: 
            return False

        vowels = set("aeiouAEIOU")
        hasVowels = False
        hasConsonant = False 

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    hasVowels = True
                else:
                    hasConsonant = True

        return hasVowels and hasConsonant


if __name__ == "__main__":
    sol = Solution()
    test_cases = {
        "abc": True,            # hợp lệ: có nguyên âm 'a', phụ âm 'b', đủ 3 ký tự
        "a1": False,            # ngắn hơn 3 ký tự
        "123": False,          # không có chữ cái
        "aE3": False,          # không có phụ âm
        "bC5": False,          # không có nguyên âm
        "Ae1": False,          # không có phụ âm
        "Bcd3": False,          # có phụ âm 'B', 'c', 'd' và nguyên âm '3' không tính → sai → thiếu nguyên âm → False
        "BcdE": True,          # có phụ âm và nguyên âm
        "abc#": False,         # ký tự đặc biệt → sai
        "aei": False,          # chỉ toàn nguyên âm → sai
        "bcd": False,          # chỉ toàn phụ âm → sai
        "aBc1": True           # hợp lệ
    }

    for word, expected in test_cases.items():
        result = sol.isValid(word)
        print(f"{word!r:8} ➜ {result} (expected: {expected}) {'✅' if result == expected else '❌'}")