import collections

class TreeNode:
    def __init__(self, color = "RED", val = 0):
        self.val = val
        self.color = color
        self.right = None
        self.left = None
        self.parent = None
    def __str__(self):
        return f"{self.val}-{self.color}"
        
class RB_Tree:
    def __init__(self):
        self.nil = TreeNode("BLACK", "nil")
        self.root = self.nil
        self.size = 0
        
    def print(self):
        if self.root == self.nil:
            print("The tree is empty.")
            return
        q = collections.deque()
        q.append((self.root, "root"))
        while q:
            node, color = q.popleft()
            print(f"{node}-{color}")
            if node.left != self.nil:
                q.append((node.left, "left"))
            if node.right != self.nil:
                q.append((node.right, "right"))
                
    def __leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        
    def __rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
        
    def __insertFixup(self, z):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                uncle = z.parent.parent.right
                if uncle.color == "RED":                      #case 1
                    z.parent.color = uncle.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent                           # case 2
                        self.__leftRotate(z)
                        
                    z.parent.color = "BLACK"                   # case 3
                    z.parent.parent.color = "RED"
                    self.__rightRotate(z.parent.parent)  
            else:
                uncle = z.parent.parent.left
                if uncle.color == "RED":                     # case 1
                    z.parent.color = uncle.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z.parent == z.parent.left:            # case 2
                        z = z.parent
                        self.__rightRotate(z)
                    z.parent.color = "BLACK"                # case 3
                    z.parent.parent.color = "RED"
                    self.__leftRotate(z.parent.parent)
        self.root.color = "BLACK"
        
    def __Transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
        
    def __deleteFixup(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == "RED":    # case 1
                    sibling.color = "BLACK"
                    x.parent.color = "RED"
                    self.__leftRotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == "BLACK" and sibling.right.color == "BLACK": # case 2
                    sibling.color = "RED"
                    x = x.parent
                else:
                    if sibling.right.color == "BLACK":   # case 3
                        sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self.__rightRotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color        # case 4
                    sibling.parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self.__leftRotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == "RED":                    # case 1
                    sibling.color = "BLACK"
                    x.parent.color = "RED"
                    self.__rightRotate(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == "BLACK" and sibling.right.color == "BLACK":   # case 2
                    sibling.color = "RED"
                    x = x.parent
                else:
                    if sibling.left.color == "BLACK":                           # case 3
                        sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self.__leftRotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color                            # case 4
                    x.parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self.__rightRotate(x.parent)
                    x = self.root
        x.color = "BLACK"
    
    def __getMinimum(self, node):
        tmp = node
        while tmp.left != self.nil:
            tmp = tmp.left
        return tmp
        
    def delete(self, val):
        y = self.root
        while y != self.nil and y.val != val:
            if val < y.val:
                y = y.left
            else:
                y = y.right
        z = y
        if y == self.nil:
            print("No such a value for delete!")
            return
        self.size -= 1
        z = y
        yOriginColor = y.color
        if y.left == self.nil:
            x = y.right
            self.__Transplant(y, x)
        elif y.right == self.nil:
            x = y.left
            self.__Transplant(y, x)
        else:
            y = self.__getMinimum(y.right)
            yOriginColor = y.color
            x = y.right
            if y != z.right:
                self.__Transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            else:
                x.parent = y
            self.__Transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if yOriginColor == "BLACK":
            self.__deleteFixup(x)


        
    def insert(self, val):
        x = self.root
        y = self.nil
        z = TreeNode("RED", val)
        self.size += 1
        while x != self.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z  ## the tree is empty
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        z.left = z.right = self.nil
        self.__insertFixup(z)

# tree = RB_Tree()
# tree.insert(5)
# tree.insert(6)
# tree.insert(4)
# tree.insert(20)
# tree.insert(23)
# print("size: ", tree.size)
# tree.print()
# tree.delete(6)
# tree.delete(5)
# print("after deleting")
# print("size: ", tree.size)
# tree.print()
