def isPalindrome(s):
    s = s.lower()
    newstring = ""
    for a in s:
        if(a.isalnum()):
            newstring += ''.join(a)
    if(newstring[::-1]==newstring):
        return True
    
    return False
        



print(isPalindrome("race a car"))