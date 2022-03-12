#only for positive powers
x=int(input("enter base value=="))
n=int(input("enter exponent value=="))
def power(x,n):
    if(n==0):
        return 1
    else:
        store=power(x,n-1)
        return x*store
print("power==",power(x,n))