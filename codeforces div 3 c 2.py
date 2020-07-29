t=int(input())
while t:
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    ans=n-1
    temp=0
    if n==1:
        print("0")
        continue
    for i in range(1,n-1):
        if arr[i]<arr[i-1] and arr[i]<=arr[i+1]:
            temp=i
    print(min(temp,ans))
    continue
