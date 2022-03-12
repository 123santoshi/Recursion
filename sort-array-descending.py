n=int(input("enter no of elements=="))
a=[int(input("")) for i in range(n)]
size=len(a)
def sort(a,size):
    if(size>1):
        mi=minindex1(a,size)
        a[size-1],a[mi]=a[mi],a[size-1]
        sort(a,size-1)
    return a
def minindex1(a,size):
    minindex=0
    min=a[0]
    for i in range(1,size):
        if(min>a[i]):
            min=a[i]
            minindex=i
    return minindex
print("array after sorting in descending order==",sort(a,size))
