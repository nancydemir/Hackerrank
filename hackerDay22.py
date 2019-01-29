class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
      
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    
    def getHeight(self,root):
        #Write your code here
        leftdepth=0
        rightdepth=0
        if root is None:
            return(0)
        else:
            if root.left != None:
                leftdepth = self.getHeight(root.left)+1
            if root.right != None:
                rightdepth = self.getHeight(root.right)+1
        if leftdepth > rightdepth:
            return(leftdepth)
        else:
            return(rightdepth)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)      
