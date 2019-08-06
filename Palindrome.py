def reverse(s):
    return s[::-1]

def ispalindrome(s):
    rev=reverse(s)
    if s==rev:
        return True
    return False

s="maheboob"
print(s)
ans=ispalindrome(s)
if ans==1:
    print(s,"is palindrome")
else:
    print(s,"is not a palindrome")

print(reverse(s))