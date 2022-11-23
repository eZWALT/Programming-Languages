
class Tree:

    def __init__(self,x):
        self.rt = x
        self.fills = []
    
    def add_child(self,a):
        self.fills = self.fills + [a]

    def root(self):
        return self.rt
    
    def num_children(self):
        return len(self.fills)
    
    def ith_child(self, i):
        return self.fills[i]

class Pre(Tree): 

    def preorder(self):

        list = [self.root()]
        for k in self.fills:
            list = list + k.preorder()

        return list

        


    
