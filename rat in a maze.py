def printans(solution):
    for i in range(len(maze)):
        print(solution[i])

def issafe(maze,x,y,solution):
    if x>=0 and x<len(maze) and y>=0 and y<len(maze) and maze[x][y]==1:
        return True
    else:
        return False
        
def solveMazeUtil(maze,x,y,solution):
    if x>=len(maze) or y>=len(maze):
        return False
    if x==len(maze)-1 and y==len(maze)-1 and maze[x][y]==1:
        solution[x][y]=1
        return True
    if issafe(maze,x,y,solution):
        solution[x][y]=1
        if solveMazeUtil(maze,x+1,y,solution): #depends upon initial ans final positions
            return True
        if solveMazeUtil(maze,x,y+1,solution):# more if conditions needed
            return True
    solution[x][y]=0
    return False
        
        
    
def solveMaze(maze):
    solution=[]
    for i in range(len(maze)):
        solution.append([0]*len(maze[0]))
    if solveMazeUtil(maze,0,0,solution):
        printans(solution)
    else:
        print("no solution")
    
    

maze = [ [1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1] ] 
solveMaze(maze)
