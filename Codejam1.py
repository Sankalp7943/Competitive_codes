t=int(input())
itr=0
while t:
    itr+=1
    t-=1
    size=int(input())
    mat = []
    rows=0
    cols=0
    diagsum=0
    sumrow=(size*(size+1))//2
    s=set()
    for i in range(size):
        mat.append(list(map(int,input().split())))

    for i in range(size):
        diagsum+=mat[i][i]

    for i in range(size):
        if len(set(mat[i]))!=size:
            rows+=1
        for j in range(size):
            s.add(mat[j][i])
            if j==size-1:
                if len(s)!=size:
                    cols+=1
                s.clear()
                
    print("Case #"+str(itr)+": "+str(diagsum)+" "+str(rows)+" "+str(cols))
    continue
            
    
