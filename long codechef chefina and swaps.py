t=int(input())
while t:
    t-=1
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    dic={}
    bool=0
    swap1=[]
    swap2=[]
    for i in range(n):
        if arr1[i] in dic:
            dic[arr1[i]]+=1
        else:
            dic[arr1[i]]=1
    for i in range(n):
        if arr2[i] in dic:
            dic[arr2[i]]-=1
        else:
            dic[arr2[i]]=-1
    for key in dic.keys():
        if dic[key]%2:
            bool=1
            break
        elif dic[key]==0:
            continue
        else:
            cnt=abs(dic[key]//2)
            while cnt:
                if dic[key]>0:
                    swap1.append(key)
                else:
                    swap2.append(key)
                cnt-=1
    if bool==1 or len(swap1)!=len(swap2):
        print("-1")
        continue
    swap1.sort()
    swap2.sort(reverse=True)
    k=len(swap1)
    cost=0
    x=min(min(arr1),min(arr2))
    for i in range(k):
        cost+=min(2*x,min(swap1[i],swap2[i]))
    print(cost)
    continue
