def reversed(s):
    return s[::-1]

def ispalindrome(s):
    rev=reversed(s)
    if s==rev:
        return True
    return False
s="maheboob"

ans=ispalindrome(s)
if ans==1:
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")
print(reversed(s))