
n=int(input())
s=str(input())
st=[]
ans=0
top=-1
for i in range(n):
    if top==-1:
        st.append(s[i])
        top+=1
    elif s[i]==st[top]:
        ans+=1
    else:
        st.append(s[i])
        top+=1
print(ans)

            
