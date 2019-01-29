class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
         
#the node object has a data field and a node instance pointer field
#the integer data value must be added to the end of the list as a new node object
#create a new node, pass "data" to the new node object,and insert to the tail end
#of the list referenced by the head parameter(transverse list to end????)
#once the new node is added, return the reference to the head node.
#insert shoud return a reference to the head node.pass "data" as the node
#constructor argument, and insert at the tail of the linked list.
            
    def insert(self,head,data):
        if head == None: # the head node is empty
            head = Node(data)#so, inset at the head
            return(head)
        elif head.next == None: #then this is the tail
            head.next = Node(data)#so,insert at the tail
        else:
            if head.next != None:
                self.insert(head.next,data) #we have to use the next value
                #of each node to get to the next node. head is the node?
        return(head)
    #Complete this method   
    
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
