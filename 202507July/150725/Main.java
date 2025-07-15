class Solution_150725 {
    public boolean isValid(String word) {
        if (word.length() < 3) return false;

        String vowels = "aeiouAEIOU";
        boolean hasVowel = false;
        boolean hasConsonant = false;

        for (char ch : word.toCharArray()) {
            if (!Character.isLetterOrDigit(ch)) return false;

            if (Character.isLetter(ch)) {
                if (vowels.indexOf(ch) >= 0) {
                    hasVowel = true;
                } else {
                    hasConsonant = true;
                }
            }
        }      
        return hasVowel && hasConsonant;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution_150725 sol = new Solution_150725();
        String[] testWords = {
            "abc", "a1", "123", "aE3", "bC5",
            "Ae1", "Bcd1", "BcdE", "abc#", "aei", "bcd", "aBc1"
        };
        boolean[] expected = {
            true, false, false, false, false,
            false, false, true, false, false, false, true
        };

        for (int i = 0; i < testWords.length; i++) {
            String word = testWords[i];
            boolean result = sol.isValid(word);
            System.out.printf("'%s' ➜ %s (expected: %s) %s\n",
                word, result, expected[i],
                result == expected[i] ? "✅" : "❌");
        }
    }
}