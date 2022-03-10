def array(n):
    if(n<=0):
        return 
    else:
        print(n)
        array(n-1) #recursively callling same function
n=int(input("enter last number in array="))
array(n)   #calling function
