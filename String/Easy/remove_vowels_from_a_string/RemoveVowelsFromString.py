# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

# Example 1:

# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"

# S consists of lowercase English letters only.
# 1 <= S.length <= 1000

class Solution:
                 
    def removeVowels(self, S: str) -> str:
        return "".join(ch for ch in S if ch not in "aeiou")
