

n,q=map(int,input().split())
h=list(map(int,input().split()))
a=list(map(int,input().split()))

bool=0
while q:
    sweet=0
    q-=1
    st=[]
    top=-1
    f=0
    lis=list(map(str,input().split()))
    if lis[0]=="2":
        end=int(lis[2])-1
        start=int(lis[1])-1
        if start==end:
            print(a[start])
            continue
        else:
            if h[end]>=h[start]:
                print("-1")
                continue
            else:
                if start>end:
                    k=-1
                else:
                    k=1
                p=start
                while True:
                    if top==-1:
                        st.append(p)
                        top+=1
                    if h[p]>h[start]:
                        f=1
                        break
                    elif h[p]==h[st[top]]: 
                        if a[p]>a[st[top]] or p==end:
                            st[top]=p
                    elif h[p]<h[st[top]]: #take care of equal condition
                        st.append(p)
                        top+=1
                    elif h[p]>h[st[top]]:
                        while top>=0 and h[p]>h[st[top]]:
                            st.pop(top)
                            top-=1
                        st.append(p)
                        top+=1
                    if p==end:
                        if st[0]!=start:
                            bool=1
                            break
                        break
                    p+=k
            if f==1:
                print("-1")
                continue
            if st[0]!=start or st[top]!=end :
                print("-1")
                continue
            else:
                while top>=0:
                    sweet+=a[st.pop(top)]
                    top-=1
            print(sweet)
            
            continue
            
    else:
        pos=int(lis[1])-1
        a[pos]=int(lis[2])
        continue
            
                    
            
            
                        
        
        
