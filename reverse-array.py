a=[4,7,2,9,8]
size=len(a)-1
def reverse(a,size):
    if(size<0):
        return
    else:
        print(a[size],end=" ")
        store=reverse(a,size-1)
reverse(a,size)

