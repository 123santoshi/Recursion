#sort array in ascending order
n=int(input("enter no of elements=="))
a=[int(input("")) for i in range(n)]
size=len(a)
def sort(a,size):
    if(size>1):
        mi=maxindex1(a,size-1) #finding index of maximum number in array
        a[size-1],a[mi]=a[mi],a[size-1]  #swap last elemnet with max index number
        sort(a,size-1)
    return a
def maxindex1(a,size):
    maxindex=0
    max=a[0]
    for i in range(1,size):
        if(max<a[i]):   #finding max number in array
            max=a[i]
            maxindex=i
    return maxindex
print("after sorting array in ascending order==",sort(a,size))