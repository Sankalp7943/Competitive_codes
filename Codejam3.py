def searchindex(Arr,idx,num,t):
    print("CALLED")
    for i in range(idx+1,len(Arr)-1):
        print(num)
        if i in Arr==num and t[i]==0:
            return int(i)


tt=int(input())
itr=0
while tt:
    itr+=1
    tt-=1
    tasks=int(input())
    mat = []
    for i in range(tasks):
        mat.append(list(map(int,(input()).split())))
    c=0
    j=0
    t=[0]*tasks
    ans=""
    res=[]
    for i in range(tasks):
        res.append(mat[i])
    mat.sort()
    for i in range(tasks):
        if mat[i][0]>=c:
            c=mat[i][1]
            idx=res.index([mat[i][0],mat[i][1]])
            if not(t[idx]!="C" or t[idx]!="J"):
                t[idx]="C"
            else:
                num=[mat[i][0],mat[i][1]]
                idx=searchindex(res,idx,num,t)
                t[idx]="C"
        elif mat[i][0]>=j:
            j=mat[i][1]
            idx=res.index([mat[i][0],mat[i][1]])
            if not(t[idx]!="C" or t[idx]!="J"):
                t[idx]="J"
            else:
                num=[mat[i][0],mat[i][1]]
                idx=searchindex(res,idx,num,t)
                t[idx]="J"
        elif mat[i][0]<c and mat[i][0]<j:
            ans="IMPOSSIBLE"
            break
    if ans=="IMPOSSIBLE":                
        print("Case #"+str(itr)+": "+ans)
    else:
        ans=""
        for i in range(len(t)):
            ans+=str(t[i])
        print("Case #"+str(itr)+": "+ans)
    continue
                
                        
            
    
