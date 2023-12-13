class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.children = children
        
    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)
            
tree = TreeNode('Transportasi',[])
darat = TreeNode('Darat',[])
laut = TreeNode('Laut',[])
udara = TreeNode('Udara',[])
tree.addChild(darat)
tree.addChild(laut)
tree.addChild(udara)
dua = TreeNode('Roda 2',[])
empat = TreeNode('Roda 4',[])
darat.addChild(dua)
darat.addChild(empat)
print(tree)
