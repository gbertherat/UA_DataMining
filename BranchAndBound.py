import math
import file as f
import copy

from Glouton import Glouton

class BranchAndBound:
    def __init__(self) -> 'BranchAndBound':
        self.upperbound = math.inf
        self.bases = []
        
    def getCost(self, selected_bases:list, bases:list) -> int:
        cost = 0;
        for i, base in enumerate(selected_bases):
            if base == True:
                cost += f.getBaseCost(bases[i].getFilename())
        return cost
        
    def start(self, scenario:int) -> int:
        path = "Scenarios/Liste_Entreprises/Liste_Ent"
        entreprises = f.getList(path, scenario)
        bases = sorted(f.getAllBasesInScenario(scenario), key=lambda x: x.getRatio(), reverse=True)
        
        selected_bases = []
        for base in bases:
            selected_bases.append(False)
            
        glouton = Glouton()
        glouton.start(scenario)
        self.upperbound = glouton.cost
        self.branchAndBound(entreprises, bases, selected_bases, 0)
            
        return self.upperbound
    
    def branchAndBound(self, entreprises:list(), bases:list(), selected_bases:list(), index:int=0) -> None:
        if index >= len(bases) \
            or self.getCost(selected_bases, bases) > self.upperbound:
                return    
        
        found_entreprises = []
        for i, base in enumerate(selected_bases):
            if base:
                for entreprise in entreprises:
                    if entreprise in found_entreprises:
                        continue
                    elif f.isEntrepriseInBase(entreprise, "Bases/" + bases[i].getFilename()):
                        found_entreprises.append(entreprise)
        
        if len(found_entreprises) == len(entreprises):
            self.upperbound = self.getCost(selected_bases, bases)
            self.bases = copy.deepcopy(selected_bases)
            return
                          
        leftBranch = copy.deepcopy(selected_bases)
        rightBranch = copy.deepcopy(selected_bases)
        
        leftBranch[index] = True
        rightBranch[index] = False
        
        self.branchAndBound(entreprises, bases, leftBranch, index + 1)
        self.branchAndBound(entreprises, bases, rightBranch, index + 1)
        
        
        
        