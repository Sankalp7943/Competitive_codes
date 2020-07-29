import heapq
def check(arr):
    heap=[]
    for i in range(len(arr)):
        heapq.heappush(heap,arr[i])
    i=0
    j=len(arr)-1
    while i!=j:
        if arr[i]<=arr[j] and arr[i]==heapq.heappop(heap):
            arr.pop(i)
            j-=1
        elif arr[i]>arr[j] and arr[j]==heapq.heappop(heap):
            arr.pop(j)
            j-=1
        else:
            return False
    return True
        
t=int(input())
while t:
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    ans=n+1
    if n==1:
        print("0")
        continue
    for i in range(n):
        if check(arr[i:n]):
            ans=i
            break
    print(min(ans,n-1))
    continue
