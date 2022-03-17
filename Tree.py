
class Tree:
    def __init__(self, entreprises, cost:int, leftNode, rightNode):
        self.cost = cost
        self.entreprises = entreprises
        self.leftNode = leftNode
        self.rightNode = rightNode 
    
    def getCost(self) -> int: 
        return self.cost

    def setCost(self, new_cost):
        self.cost = new_cost
    
    def getEntreprise(self): 
        return self.entreprises

    def addEntrprise(self, entreprise):
        self.entreprises.append(entreprise)

    def getLeftNode(self): 
        return self.leftNode
    
    def setLeftNode(self, leftNode):
        self.leftNode = leftNode
        
    def getRightNode(self): 
        return self.rightNode
    
    def setRightNode(self, rightNode):
        self.rightNode = rightNode