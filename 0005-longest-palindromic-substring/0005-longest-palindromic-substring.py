class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        
        for i in range(len(s)):
            palindrome1 = expandAroundCenter(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1
           
            palindrome2 = expandAroundCenter(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2
        
        return longest