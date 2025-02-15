class treeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
    def __str__(self,level=0):
        ret=" "* level+str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret
    def addChild(self,treeNode):
        self.children.append(treeNode)
tree=treeNode('Drinks',[])
cold=treeNode('cold',[])
hot=treeNode('Hot',[])
tree.addChild(cold)
tree.addChild(hot)
tea=treeNode('Tes',[])
coffee=treeNode('Coffee',[])
cola=treeNode('cola',[])
fanta=treeNode('fanta',[])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)