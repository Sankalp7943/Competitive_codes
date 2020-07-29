t=int(input())
while t:
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    i=0
    j=1
    moves=0
    if n==1:
        if arr[0]%2:
            print("-1")
            continue
        else:
            print("0")
            continue
    while i<n:
        if arr[i]%2:
            while j<n:
                if arr[j]%2==0:
                    arr[i],arr[j]=arr[j],arr[i]
                    moves+=1
                    break
                j+=2
        
        i+=2
    for i in range(n):
        if i%2==0 and arr[i]%2==1:
            moves=-1
    print(moves)
    continue
