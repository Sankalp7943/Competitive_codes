t=int(input())
while t:
    t-=1
    n=int(input())
    dicx={}
    dicy={}
    for i in range((4*n)-1):
        x1,y1=map(int,input().split())
        if x1 in dicx:
            dicx[x1]+=1
        else:
            dicx[x1]=1
        if y1 in dicy:
            dicy[y1]+=1
        else:
            dicy[y1]=1
    for key in dicx.keys():
        if dicx[key]%2:
            x=key
            break
    for key in dicy.keys():
        if dicy[key]%2:
            y=key
            break
    print(str(x)+" "+str(y))
    continue
