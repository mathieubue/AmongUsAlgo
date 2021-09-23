
class Player:
    id=1
    def __init__(self):
        self.id = Player.id
        self.score = 0
        Player.id += 1
    
    def to_string(self):
        return "Id : " + str(self.id) + "\n" + "Score : " + str(self.score)
    
class Node :
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1
        
class Tree : 
    def __init__(self,root=None):
        self.root = root

    def insert(self,root,key):
        #step1
        if root == None:
            return Node(key) 
        elif key.score < root.val.score :
            root.left = self.insert(root.left, key)
        else :
            root.right = self.insert(root.right, key)
        
            
        
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right))
        
         # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key.score <= root.left.val.score: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key.score >= root.right.val.score: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key.score > root.left.val.score: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key.score < root.right.val.score: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
        
        return root 
    
    def delete(self, root, key): 
  
        # Step 1 - Perform standard BST delete 
        if root==None: 
            return root 
  
        elif key.score < root.val.score: 
            root.left = self.delete(root.left, key) 
  
        elif key.score > root.val.score: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, 
                                      temp.val) 
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
    
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.getMinValueNode(root.left) 
    
######
# Python3 Program to print binary tree in 2D  
COUNT = [10]  

# Function to print binary tree in 2D  
# It does reverse inorder traversal  
def print2DUtil(root, space) : 
  
    # Base case  
    if (root == None) : 
        return
  
    # Increase distance between levels  
    space += COUNT[0] 
  
    # Process right child first  
    print2DUtil(root.right, space)  
  
    # Print current node after space  
    # count  
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ")  
    print(root.val.score)  
  
    # Process left child  
    print2DUtil(root.left, space)  
  
# Wrapper over print2DUtil()  
def print2D(root) : 
      
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)  
#####


def AVL_from_list(list):
   root = Node(list[0])
   tree = Tree(root)
   for index in range (1,len(list)) :
      tree.insert(root, list[index])
   return tree
                
            
def PreOrder(root):
    curr = root
    if(curr==None):
        return
    else:
        print(curr.val.to_string())
        PreOrder(curr.left)
        PreOrder(curr.right)

def PostOrder(root):
    curr = root
    if(curr==None):
        return
    else:
        PostOrder(curr.left)
        PostOrder(curr.right)
        print(curr.val.to_string())

def InOrder(root):
    curr = root
    if(curr==None):
        return
    else:
        InOrder(curr.left)
        print(curr.val.to_string())
        InOrder(curr.right)

def search(root,score):   
    if root is None or root.val.score == score:
        return root     
    if root.val.score < score:
        return search(root.right,score)      
    return search(root.left,score)

