a,b,c=0,1,1
def fib(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return fib(n-1) + fib(n-2)
n=int(input("enter nth number=="))
ans=fib(n-1)
print("{0} number of fibnonaci seriess={1}".format(n,ans))
