class Solution:
    def isPalindrome(self, s: str) -> bool:
        complited=""
        for ch in s:
            if ch.isalnum():
                complited+=ch.lower()
        return complited==complited[::-1]

        