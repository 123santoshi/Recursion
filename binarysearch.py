n=int(input("enter no of elements=="))
a=[int(input("enter array values==")) for i in range(n)]
key=int(input("enter key value=="))
low=0
high=len(a)-1
def bs(a,low,high,key):
    if(low<=high):
        mid=(low+high)//2
        if(a[mid]==key):
            return mid
        elif(a[mid]>key):
            store=bs(a,low,mid-1,key)
        else:
            store=bs(a,mid+1,high,key)
    else:
        return -1
    return store
ans=bs(a,low,high,key)
if(ans==-1):
    print("key is not found")
else:
    print("key is found at position {0}".format(ans))




