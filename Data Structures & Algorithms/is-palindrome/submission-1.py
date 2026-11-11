class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string = new_string + char.lower()
            reversed_string = "".join(reversed(new_string))
        return new_string == reversed_string