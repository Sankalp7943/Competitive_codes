t=int(input())
while t:
    t-=1
    arr=list(map(int,input().split()))
    if arr[0]!=arr[1] and arr[1]!=arr[2] and arr[0]!=arr[2]:
        print("NO")
        continue
    if arr[0]==arr[1] and arr[1]==arr[2]:
        print("YES")
        k=arr[0]
        print(str(k)+" "+str(k)+" "+str(k))
        continue
    if arr[0]==arr[1]:
        k=arr[0]
        if max(arr)==k:
            print("YES")
            print(str(k)+" "+str(min(arr))+" "+str(min(arr)))
            continue
        else:
            print("NO")
            continue
    if arr[1]==arr[2]:
        k=arr[1]
        if max(arr)==k:
            print("YES")
            print(str(k)+" "+str(min(arr))+" "+str(min(arr)))
            continue
        else:
            print("NO")
            continue
    if arr[0]==arr[2]:
        k=arr[0]
        if max(arr)==k:
            print("YES")
            print(str(k)+" "+str(min(arr))+" "+str(min(arr)))
            continue
        else:
            print("NO")
            continue
