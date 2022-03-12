n=int(input("enter number=="))
rev=0
def palindrome(n,rev):
    if(n==0):
        return rev
    else:
        r=n%10
        rev=rev*10+r
        store=palindrome(n//10,rev)
        return store
ans=palindrome(n,rev)
if(ans==n):
    print("Given number {0} is palindrome".format(n))
else:
    print("Given number {0} is not palindrome".format(n))