using System;
using System.Collections.Generic;

public class Solution
{
    public bool IsValid(string word)
    {
        if (word.Length < 3) return false;

        HashSet<char> vowels = new HashSet<char>
        {
            'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
        };

        bool hasVowel = false;
        bool hasConsonant = false;

        foreach (char ch in word)
        {
            if (!char.IsLetterOrDigit(ch)) return false;

            if (char.IsLetter(ch))
            {
                if (vowels.Contains(ch))
                {
                    hasVowel = true;
                }
                else
                {
                    hasConsonant = true;
                }
            }
        }

        return hasVowel && hasConsonant;
    }
}


public class Program
{
    public static void Main()
    {
        var sol = new Solution();
        var testCases = new Dictionary<string, bool> {
            { "abc", true },
            { "a1", false },
            { "123", false },
            { "aE3", false },
            { "bC5", false },
            { "Ae1", false },
            { "Bcd3", false },
            { "BcdE", true },
            { "abc#", false },
            { "aei", false },
            { "bcd", false },
            { "aBc1", true }
        };

        foreach (var kv in testCases) {
            var result = sol.IsValid(kv.Key);
            Console.WriteLine($"'{kv.Key}' ➜ {result} (expected: {kv.Value}) {(result == kv.Value ? "✅" : "❌")}");
        } 
    }
}