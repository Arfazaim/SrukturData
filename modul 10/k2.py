class TreeNode:
    def __init__(self,data):
        self.data = data;
        self.leftChild = None
        self.rightChild = None
        
    def preOrderTraversal(root_node):
        if not root_node:
            return
        print(root_node.data)
        preOrderTraversal(root_node.leftChild)
        preOrderTraversal(root_node.rightChild)
        
    def inOrderTraversal(root_node):
        if not root_node:
            return
        inOrderTraversal(root_node.leftChild)
        print(root_node.data)
        inOrderTraversal(root_node.rightChild)
        
    def postOrderTraversal(root_node):
        if not root_node:
            return
        postOrderTraversal(root_node.leftChild)
        postOrderTraversal(root_node.rightChild)
        print(root_node.data)