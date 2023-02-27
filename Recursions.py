##Palindrome

def isPalindrome(s):
    """Return true if S is a palindrom and False otherwise"""

    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])
