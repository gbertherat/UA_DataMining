
class Node:
    def __init__(self, entreprises:list=[], cost:int=0, children:list=[]):
        self.cost = cost
        self.entreprises = entreprises
        self.children = children
    
    def getCost(self) -> int: 
        return self.cost

    def setCost(self, new_cost) -> None:
        self.cost = new_cost
    
    def getEntreprises(self) -> list: 
        return self.entreprises

    def addEntreprise(self, entreprise) -> None:
        self.entreprises.append(entreprise)
        
    def getChildren(self) -> list:
        return self.children
    
    def addChild(self, child:'Node') -> None:
        self.children.append(child)
    