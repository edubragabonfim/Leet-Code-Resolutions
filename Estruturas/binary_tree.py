class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
        
    def preorder_transversal(self):  # Root é o primeiro elemento do array
        result = []
        self._preorder_transversal_recursive(self.root, result)
        return result
    
    def _preorder_transversal_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_transversal_recursive(node.left, result)
            self._preorder_transversal_recursive(node.right, result)

    def inorder_transversal(self):  # Root é o elemento do meio do array
        result = []
        self._inorder_transversal_recursive(self.root, result)
        return result
    
    def _inorder_transversal_recursive(self, node, result):
        if node:
            self._inorder_transversal_recursive(node.left, result)
            result.append(node.data)
            self._inorder_transversal_recursive(node.right, result)

    def postorder_transversal(self):  # Root é o último elemento do array
        result = []
        self._postorder_transversal_recursive(self.root, result)
        return result
    
    def _postorder_transversal_recursive(self, node, result):
        if node:
            self._postorder_transversal_recursive(node.left, result)
            self._postorder_transversal_recursive(node.right, result)
            result.append(node.data)
    
            

bt = BinaryTree()

bt.insert(5)
bt.insert(3)
bt.insert(1)
bt.insert(10)
bt.insert(15)
bt.insert(7)

print(bt.search(5))
print(bt.search(12))

print(f'preorder_transversal: {bt.preorder_transversal()}')
print(f'inorder_transversal: {bt.inorder_transversal()}')
print(f'postorder_transversal: {bt.postorder_transversal()}')