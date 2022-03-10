n=int(input("enter number=="))
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
ans=fact(n)
print("factorail of {0} is {1}".format(n,ans))
