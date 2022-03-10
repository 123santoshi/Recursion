n=int(input("enter number=="))
s=0
def product(n):
    if(n<=0):
        return 1
    else:
        s=n%10
        return s*product(n//10)
print("product of digits in n=",product(n))