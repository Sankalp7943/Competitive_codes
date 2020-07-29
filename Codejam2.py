t=int(input())
itr=0
while t:
    itr+=1
    t-=1
    num=str(input())
    string=""
    op=0
    for i in range(len(num)):
        if num[i]=="0":
            while op>0:
                string=string+")"
                op-=1
            if op==0:
                string=string+num[i]
        else:
            if op<int(num[i]):
                while op<int(num[i]):
                    string=string+"("
                    op+=1
            elif op>int(num[i]):
                while op>int(num[i]):
                    string=string+")"
                    op-=1
            if op==int(num[i]):
                string=string+num[i]
    if op>0:
        while op>0:
            string=string+")"
            op-=1
    print("Case #"+str(itr)+": "+str(string))
    continue
            
    
