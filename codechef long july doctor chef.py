def daycal(k,x):
    cnt=0
    while k>x:
        cnt+=1
        x*=2
    return cnt+1

t=int(input())
while t:
    t-=1
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    days=0
    arr.sort()
    i=0
    while i<n:
        if arr[i]==x:
            days+=1
            arr[i]=0
            x*=2
        elif i==0 and arr[i]>x:
                days+=daycal(arr[i],x)
                x=arr[i]*2
                arr[i]=0
        elif i>0 and i<n and arr[i-1]<x<arr[i]:
            if arr[i-1]*2>=arr[i]:
                i-=1
                days+=daycal(arr[i],x)
                x=arr[i]*2
                arr[i]=0
            else:
                days+=daycal(arr[i],x)
                x=arr[i]*2
                arr[i]=0        
        i+=1
    for i in range(n):
        if arr[i]:
            days+=1
    print(days)
    continue
