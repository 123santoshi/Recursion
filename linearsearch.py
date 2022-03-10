n=int(input("enter no of elements=="))
a=[int(input("enter array values==")) for i in range(n)]
key=int(input("enter serach element="))
index=len(a)-1
def ls(a,index,key):
    if(index>=0):
        if(a[index]==key):
            return index
        else:
            #print("i==",index)
            store=ls(a,index-1,key)
    else:
        return -1
    return store
size=ls(a,index,key)
if(size==-1):
    print("element is not found")
else:
    print("element is found at position {0}".format(size))