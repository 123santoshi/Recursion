n=int(input("enter no of elements=="))
a=[int(input("")) for i in range(n)]
i=0
def square(a,i):
    if(i==len(a)):
        return 
    else:
        print("the element {0} after  squaring=={1}".format(a[i],a[i]*a[i]))
        square(a,i+1)
    
square(a,i)
