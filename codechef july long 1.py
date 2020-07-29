t=int(input())
while t:
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    for i in range(1,n):
        if not abs(arr[i-1]-arr[i])<=1:
            ans+=abs(arr[i-1]-arr[i])-1
    print(ans)
    continue
