t=int(input())
while t:
    t-=1
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    ans=0
    i=0
    while i<n:
        if arr[i]>=x:
            ans+=1
        else:
            if x%arr[i]==0 and x//arr[i]<=n-i:
                ans+=1
            elif x%arr[i] and (x//arr[i])+1<=n-i:
                ans+=1
        i+=1     
    print(ans)
    continue
