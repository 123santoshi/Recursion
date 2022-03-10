a=[1,2,4,6,9,10,23]
index=0
def sorted(a,index):
    if(index==len(a)-1):
        return 1
    elif(a[index]<a[index+1]):
        store=sorted(a,index+1)
    else:
        return -1
    return store
ans=sorted(a,index)
if(ans==1):
    print("given {0} is sorted array".format(a))
else:
    print("given {0} is not sorted array".format(a))
