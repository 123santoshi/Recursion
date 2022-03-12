n=int(input("enter number=="))
rev=0
def reverse(n,rev):
    if(n==0):
        return rev
    else:
        r=n%10
        rev=rev*10+r
        store=reverse(n//10,rev)
        return store
print("reverse of a number==",reverse(n,rev))