t=int(input())
while t:
    t-=1
    A=str(input())
    B=str(input())
    C=str(input())
    
    a=list(A)
    b=list(B)
    c=list(C)
    length=len(a)
    for i in range(length):
        if a[i]==b[i] and b[i]==c[i]:
            continue
        elif c[i]==b[i]:
            temp=a[i]
            a[i]=c[i]
            c[i]=temp
            continue
        else:
            temp=b[i]
            b[i]=c[i]
            c[i]=temp
            continue
    check1=""
    check2=""
    
    if (check1.join(a)==check2.join(b)):
        print("YES")
        continue
    else:
        print("NO")
        continue
            
        
