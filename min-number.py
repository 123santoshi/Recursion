n=int(input("enter no of elements=="))
a=[int(input("enter array values==")) for j in range(n)]
i=0
def minimum(a,i):
    if(i==len(a)-1):
        return a[len(a)-1]
    else:
        store=minimum(a,i+1)
        if(a[i]<store):
            return a[i]
        else:
            return store
print("minimum number in given array==",minimum(a,i))