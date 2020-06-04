# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        for i in range(len(s)):
        
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
        # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        #check if "i" has crossed middle element and if length of largest 
        #palindrome till found, is greater than half of total length of string
        #then break, we've found the answer no need to iterate more
            if (i>(len(s)//2) and len(res)>(len(s)//2)):
                break
        return res
 

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]