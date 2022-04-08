import math
import file as f
import copy

from glouton import Glouton

class BranchAndBound:
    def __init__(self) -> 'BranchAndBound':
        self.upperbound = math.inf
        self.bases = []
        
    def getCost(self, selected_bases:list, bases:list) -> int: # Permet de récupérer le coût pour chaque bases retenues
        cost = 0
        for i, base in enumerate(selected_bases):
            if base == True:
                cost += f.getBaseCost(bases[i].getFilename())
        return cost
        
    def start(self, scenario:int) -> int:
        path = "Scenarios/Liste_Entreprises/Liste_Ent"
        entreprises = f.getList(path, scenario)
        bases = sorted(f.getAllBasesInScenario(scenario), key=lambda x: x.getRatio(), reverse=True)
        
        selected_bases = []
        for base in bases: # Pour chaque bases à évaluer
            selected_bases.append(False) # On créé une liste de booléen pour dire si on prends la base ou non
            
        glouton = Glouton()
        glouton.start(scenario) # On lance le glouton
        self.upperbound = glouton.cost # Le upperbound correspond au résultat du glouton
        self.branchAndBound(entreprises, bases, selected_bases, 0) # On lance l'algorithme de Branch & Bound
            
        return self.upperbound
    
    def branchAndBound(self, entreprises:list(), bases:list(), selected_bases:list(), index:int=0) -> None:
        if index >= len(bases) \
            or self.getCost(selected_bases, bases) > self.upperbound: # Si on dépasse le upperbound en cout ou si on a plus de base à vérifier, on s'arrête
                return    
        
        found_entreprises = []
        for i, base in enumerate(selected_bases): # Pour chaque base
            if base: # Si on prends la base
                for entreprise in entreprises: # On vérifie si y'a les entreprises cherchées dans la base 
                    if entreprise in found_entreprises: # Si on a déjà l'entreprise on passe
                        continue
                    elif f.isEntrepriseInBase(entreprise, "Bases/" + bases[i].getFilename()):
                        found_entreprises.append(entreprise)
        
        if len(found_entreprises) == len(entreprises): # Si on a trouvé toutes les entreprises 
            self.upperbound = self.getCost(selected_bases, bases) # On met à jour le upperbound
            self.bases = copy.deepcopy(selected_bases) # Et récupère les bases sélectionnées
            return
                          
        leftBranch = copy.deepcopy(selected_bases)
        rightBranch = copy.deepcopy(selected_bases)
        
        leftBranch[index] = True # La branche de gauche, on prends la base
        rightBranch[index] = False # La branche de droite, on prends pas la base
        
        self.branchAndBound(entreprises, bases, leftBranch, index + 1) # On appelle récursivement la fonction en partant sur la branche de gauche
        self.branchAndBound(entreprises, bases, rightBranch, index + 1) # On appelle récursivement la fonction en partant sur la branche de droite
        
        
        
        