
class Base:
    def __init__(self, filename:str, cost:int, entreprises:list):
        self.filename = filename
        self.cost = cost
        self.entreprises = entreprises
    
    def getFilename(self) -> str:
        return self.filename

    def getCost(self) -> int:
        return self.cost
    
    def getEntreprises(self) -> list:
        return self.entreprises
    
    def getRatio(self) -> int:
        if self.cost != 0:
            return round(len(self.entreprises)/self.cost, 4)
        else:
            return 0