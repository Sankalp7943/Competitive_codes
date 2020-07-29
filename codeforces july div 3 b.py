t=int(input())
while t:
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    s=set()
    ans=[]
    for i in range(2*n):
        if arr[i] not in s:
            s.add(arr[i])
            ans.append(arr[i])
    res=""
    for i in range(len(ans)):
        res+=str(ans[i])+" "
    print(res[0:len(res)-1])
    continue
