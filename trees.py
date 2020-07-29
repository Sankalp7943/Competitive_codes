class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data
    def deletefound(root,data):
        return

        
    def delete(root,data):
        if root is None:
            return
        if root.findval(data)!="found":
            root.deletefound(data)
        else:
            print("Node not present")
        return

    def findval(root,data):
        if root is None:
            print("not found")
            return
        else:
            if root.val==data:
                print("found")
            elif root.val>data and root.left:
                root.left.findval(data)
                return
            elif root.val<data and root.right:
                root.right.findval(data)
                return
            else:
                print("not found")
                return
            
    def insert(root,data):
        if root:#root
            if root.val>=data:
                if root.left is None:
                    root.left=Node(data)
                    return
                else:
                    root.left.insert(data)
            else:
                if root.right is None:
                    root.right=Node(data)
                    return
                else:
                    root.right.insert(data)
    def printpreorder(root): #preorder root left right
        if not root:
            return
        print(root.val)
        if root.left:
            root.left.printpreorder()
        if root.right:
            root.right.printpreorder()
        

    def printtree(root): #inorder
        if root.left:
            root.left.printtree()
        print(root.val)
        if root.right:  
            root.right.printtree()

    def printpostorder(root):
        if not root:
            return
        if root.left:
            root.left.printpostorder()
        if root.right:
            root.right.printpostorder()
        print(root.val)
        
        
root=Node(50) #call through this object only
root.insert(20)
root.insert(30)
root.insert(10)
root.insert(70)
root.insert(60)
root.insert(80)
print("inorder")
root.printtree()

#root.findval(7)
#oot.findval(14)
print("preorder")
root.printpreorder()
print("postorder")
root.printpostorder()
