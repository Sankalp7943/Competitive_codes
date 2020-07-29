def power(k):
    string=str(k)
    res=0
    for i in range(len(string)):
        res+=int(string[i])
    return res
    
t=int(input())
while t:
    t-=1
    arr1=[]
    arr2=[]
    chef=0
    morty=0
    n=int(input())
    for i in range(n):
        temp1,temp2=map(int,input().split())
        arr1.append(temp1)
        arr2.append(temp2)
    for i in range(n):
        if power(arr1[i])>power(arr2[i]):
            chef+=1
        elif power(arr1[i])<power(arr2[i]):
            morty+=1
        else:
            chef+=1
            morty+=1
    if chef>morty:
        print("0 "+str(chef))
    elif morty>chef:
        print("1 "+str(morty))
    else:
        print("2 "+str(chef))
    
