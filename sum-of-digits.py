n=int(input("enter number=="))
s=0
def sum(n):
    if(n<=0):
        return 0
    else:
        s=n%10
        return s+sum(n//10)
print("sum of digits==",sum(n))