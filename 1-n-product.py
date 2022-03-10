n=int(input("enter n value=="))
def product(n):
    if(n==0):
        return 1
    else:
        return n*product(n-1)

print("product of first n numbers==",product(n))