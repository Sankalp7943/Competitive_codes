#importing text file into list of strings
filename=str(input("enter file name within the directory with extension")
if filename[len(filename)-4:len(filename)]!=".txt"
    print("wrong file extension")
    exit
words=[k for k in open(filename).read().split(' ')]

#page width input
width=int(input())
print(width)

INF=9999

#badness=(pagewidth-wordwidthintheline)**3
#cube is used to magnify the small difference as well can be used to check if value is -ve
def cost(i,j,width):
    if j<i:
        return width**3
    w=words[i:j+1]
    spaces=len(w)-1
    #number of spaces to be added
    total=spaces
    #total is length of line with spaces
    for k in w:
        total+=len(k)
    if total>width:
        return INF
    if j==len(words)-1:
        return 0
    return (width-total)**3

#goal is to minimise the cost cumulatively for every line
mat=[]
for i in range(0,len(words)):
    mat.append([])
    for j in range(0,len(words)):
        mat[-1].append(0)
print(mat)
for i in range(0,len(words)):
    for j in range(i,len(words)):
        mat[i][j]=cost(i,j,width)
#computing cost of every words which could be fitted into the given width

ans=[0]*len(words)
ans[0]=(width-len(words[0]))**3
for i in range(1,len(words)):
    possible=ans[i-1]+cost(i,i,width)
    for j in range(0,i):
        possible.append(sum(ans[0:j]+mat[j][i]) #sum of badness
    ans[i]=min(possible) #minimisation of badness
print("Cost is",ans[-1])
    
