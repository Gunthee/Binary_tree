#structure
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
         

    def insert(self,data):
        if self.data is None:
            self.data = data 
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                    
# insert data
list = [50,25,75,30,60,40] 

root = Node(list[0])

for i in list:
    root.insert(i)
print(f'insert value:{list}')

#print in-ordder (Infix): left, root, right
inorder_list = []
def inorder(r):
    
    if r is None:
        return
    else:
        inorder(r.left)              #left
        inorder_list.append(r.data)  #root
        inorder(r.right)             #right     
inorder(root)
print(f'In order:{inorder_list}')  

#pre-order (Prefix): root, left ,right
preorder_list = []
def preorder(s):
    if s is None:
        return
    else:
        preorder_list.append(s.data)     #root
        preorder(s.left)                 #left
        preorder(s.right)                #right
preorder(root)
print(f'Pre order:{preorder_list}')

#Postorder (Postfix): left, right, root
postorder_list = []
def postorder(t):
    if t is None:
        return
    else:
        postorder(t.left)               #left
        postorder(t.right)              #right
        postorder_list.append(t.data)   #root 
postorder(root)
print(f'Post order:{postorder_list}')



