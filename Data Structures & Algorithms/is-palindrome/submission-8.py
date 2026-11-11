class Solution:
    def isPalindrome(self, s: str) -> bool:
        #First you want to filter string by making everything lower if it is a character
        filter_string = "".join(char.lower() for char in s if char.isalnum())
        #Reverse the string and join together
        reversed_string = "".join(reversed(filter_string))
        #If the two strings =, return True, else return False
        return reversed_string == filter_string

        