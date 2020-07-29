


t=int(input())
while t:
    t-=1
    n=int(input())
    arr=[]
    for i in range(8):
        temp=["."]*8
        arr.append(temp)
    quo=n//8
    remain=n%8
    if quo==8:
        arr[0][0]="O"
        for i in range(8):
            print("".join(arr[i]))
        continue
    
    for i in range(quo):
        for j in range(8):
            arr[i][j]="*"
    
    i=quo
    j=0
    cnt=remain
    while j<8:
        if cnt:
            arr[i][j]="*"
            cnt-=1
        else:
            if quo==0:
                arr[i][j]="X"
                break
            else:
                arr[i][j]="X"
        j+=1
    i=quo+1
    j=0
    while i<8 and j<8 and j<=remain:
        arr[i][j]="X"
        j+=1
    for i in range(8):
        for j in range(8):
            if arr[i][j]=="*":
                arr[i][j]="."
    arr[0][0]="O"
    for i in range(8):
        print("".join(arr[i]))
        
    continue
    
            
    
        
    
    
        
    
