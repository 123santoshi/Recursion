n=int(input("enter number which table u want=="))
stop=int(input("enter stop value=="))
i=1
def table(n,i):
    if(i>stop):
        return 
    else:
        print("{0} * {1} = {2}".format(n,i,n*i))
        table(n,i+1)
        
table(n,i)