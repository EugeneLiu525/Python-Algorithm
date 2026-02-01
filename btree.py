class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        # Simple level order insertion (not necessarily balanced)
        queue = [node]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = TreeNode(key)
                break
            else:
                queue.append(temp.left)
            
            if not temp.right:
                temp.right = TreeNode(key)
                break
            else:
                queue.append(temp.right)

    def delete(self, key):
        if self.root is None:
            return False

        if self.root.left is None and self.root.right is None:
            if self.root.val == key:
                self.root = None
                return True
            else:
                return False

        # Find the node to delete and the last node
        queue = [self.root]
        to_delete = None
        last_node = None
        while queue:
            last_node = queue.pop(0)
            if last_node.val == key:
                to_delete = last_node
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

        if to_delete:
            to_delete.val = last_node.val  # Copy the last node's value to the node to delete
            self._delete_deepest(self.root, last_node)  # Delete the deepest rightmost node
            return True

        return False

    def _delete_deepest(self, root, d_node):
        queue = [root]
        while queue:
            temp = queue.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    queue.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    queue.append(temp.left)

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
    bt = BinaryTree()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    print("Inorder traversal:")
    bt.inorder_print(bt.root)
    print("\nPreorder traversal:")
    bt.preorder_print(bt.root)
    print("\nDeleting 2...")
    bt.delete(2)
    print("Inorder traversal:")
    bt.inorder_print(bt.root)
    print("\nPreorder traversal:")
    bt.preorder_print(bt.root)
