def parenthesis(string,n):
    if n>0:
        ans(string,0,n,0,0)

def ans(string,index,n,op,cl):
    if cl==n:
        for i in string:
            print(i, end="")
        print()
        
        return
    else:
        if op>cl:
            string[index]=")"
            ans(string,index+1,n,op,cl+1)
        if op<n:
            string[index]="("
            ans(string,index+1,n,op+1,cl)
        
        


n=int(input())
string=[""]*2*n
parenthesis(string,n)
