import file as f

class Glouton:
    def __init__(self) -> 'Glouton':
        self.bases = []
        self.cost = 0

    def start(self, scenario:int) -> None:
        bases = sorted(f.getAllBasesInScenario(scenario), key=lambda x: x.getRatio(), reverse=True) # On trie la liste des bases par l'heuristique
        
        path = "Scenarios/Liste_Entreprises/Liste_Ent"
        entreprises = f.getList(path, scenario) # On récupère la liste des entreprises recherchées
            
        i = 0
        while i < len(bases) and len(entreprises) > 0: # Pour chaque bases et tant que notre liste d'entreprises recherchées n'est pas vide
            best_base = bases[i] # On prends la base i
            basepath = "Bases/"+best_base.getFilename()
            
            new_entreprises = []
            for entreprise in entreprises: # Pour chaque entreprise recherchées
                if not f.isEntrepriseInBase(entreprise, basepath): # Si l'entreprise ne se trouve pas dans la base
                    new_entreprises.append(entreprise) # On l'ajoute à notre liste d'entreprises recherchées pour la prochaine itération
                    
            if len(new_entreprises) != len(entreprises):
                self.bases.append(best_base.getFilename()) # On ajoute la base trouvé à notre liste de résultats
                self.cost += best_base.getCost() # On ajoute le cout à notre cout total
            
            entreprises = list.copy(new_entreprises)
            i+=1