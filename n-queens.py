def iscorrect(arr,row,col):
    #row
    for i in range(col):
        if arr[row][i]==1:
            return False
    #upper diag
    i,j=row,col
    while i>=0 and j>=0:
        if arr[i][j]==1:
            return False
        i-=1
        j-=1
    #lower diagnol
    i,j=row,col
    while i<len(arr) and j<len(arr):
        if arr[i][j]==1:
            return False
        i+=1
        j-=1
    return True

def queens(queen,arr,n):
    if queen==n:
        return True
    for row in range(n):
        if iscorrect(arr,row,queen): #col=queen here
            arr[row][queen]=1
            #solve for next queen
            if queens(queen+1,arr,n):
                return True
            else:
                arr[row][queen]=0
            
    return False

def solve(n,arr):
    if queens(0,arr,n):
        for i in range(n):
            print(arr[i])
    else:
        print("no solutions")


    


  
#column wise enter
n=int(input())
arr=[]
for i in range(n):
    arr.append([0]*n)


solve(n,arr)


