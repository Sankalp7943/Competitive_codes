def printans(a,n,i):
    permute(a,n,0)
    
def permute(a,n,i):
    if i==n:
        print(a)
        return
    for x in range(i,n):
        a[x],a[i]=a[i],a[x]
        permute(a,n,i+1)
        
        a[x],a[i]=a[i],a[x]
    




a=[1,2,3]
n=len(a)
printans(a,n,0)
