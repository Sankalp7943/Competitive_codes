x=int(input())
ans=0
for i in range(x):
    temp=list(map(int,input().split()))
    if sum(temp)>1:
        ans+=1
print(ans)
    #mat.append(temp)
