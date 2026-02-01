class AVLNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)
        
        # Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        
        # Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        
        # Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def delete(self, root, key):
        if not root:
            return root

        elif key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
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
            root.right = self.delete(root.right, temp.val)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))
        return x

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def inorder_print(self, node):
        if node:
            self.inorder_print(node.left)
            print(node.val, end=' ')
            self.inorder_print(node.right)

    def preorder_print(self, node):
        if node:
            print(node.val, end=' ')
            self.preorder_print(node.left)
            self.preorder_print(node.right)
if __name__ == "__main__":
    # Example usage
    avl_tree = AVLTree()
    root = None
    root = avl_tree.insert(root, 10)
    root = avl_tree.insert(root, 20)
    root = avl_tree.insert(root, 30)
    print("Inorder traversal of AVL tree is")
    avl_tree.inorder_print(root)
    print("\nPreorder traversal of AVL tree is")
    avl_tree.preorder_print(root)
    print("\nDeleting 20...")
    avl_tree.delete(root,20)
    print("Inorder traversal of AVL tree is")
    avl_tree.inorder_print(root)
    print("\nPreorder traversal of AVL tree is")
    avl_tree.preorder_print(root)
