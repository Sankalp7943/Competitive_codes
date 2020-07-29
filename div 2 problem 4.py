n=int(input())
m=int(input())
k=int(input())
moveschange=0
movesleft=k
directmove=0
limit=(4*n*m)-(2*n)-(2*m)
seq=[]
xpos="L"
ypos="U"
if k>limit:
    print("NO")
else:
    while movesleft:
        if n>1 and xpos=="L":
            moveschange+=1
            seq.append(str(str(min(n,movesleft))+"R"))
            movesleft=movesleft-min(n,movesleft)-1
            xpos="R"
            if movesleft>1 and xpos=="R":
                moveschange+=1
                seq.append(str(str(min(n,movesleft))+"L"))
                movesleft=movesleft-min(n,movesleft)-1
                xpos="L"
            if movesleft>=1:
                moveschange+=1
                seq.append("1D")
                movesleft-=1
                xpos="L"
                continue
        else:
            moveschange+=1
            seq.append(str(str(min(m,movesleft))+"D"))
            movesleft=movesleft-min(m,movesleft)-1
            ypos="D"
            if movesleft>1 and ypos=="D":
                moveschange+=1
                seq.append(str(str(min(m,movesleft))+"U"))
                movesleft=movesleft-min(m,movesleft)-1
                ypos="U"
            if movesleft>=1:
                moveschange+=1
                seq.append("1R")
                movesleft-=1
                continue
print("YES")
print(moveschange)
for i in range(len(seq)):
    print(seq[i])
                
            
    
            
        
    
    
