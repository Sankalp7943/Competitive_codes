def search(arr,start,end,qualify):
    if start==end:
        return start
    else:
        mid=(start+end)//2
        if arr[mid]==qualify and arr[mid+1]!=qualify:
            return mid
        elif arr[mid]==qualify and arr[mid+1]==qualify:
            start=mid+1
        elif arr[mid]!=qualify:
            if arr[mid]>qualify:
                start=mid+1
            else:
                end=mid-1
        return search(arr,start,end,qualify)

lis1=list(map(int,input().split()))
n=lis1[0]
k=lis1[1]
arr=list(map(int,input().split()))

if k==n and arr[k-1]!=0:
    print(n)
else:
    qualify=arr[k-1]
    if qualify==0:
        if arr[0]==0:
            print("0")
        else:
            cnt=0
            for i in range(k):
                if arr[i]>0:
                    cnt+=1
            print(cnt)
    else:
        k=search(arr,0,len(arr)-1,qualify)
        print(k+1)
        
        
    
    
