import file as f

class Glouton:
    def __init__(self) -> 'Glouton':
        self.bases = []
        self.cost = 0

    def start(self, scenario:int) -> None:
        bases = sorted(f.getAllBasesInScenario(scenario), key=lambda x: x.getRatio(), reverse=True)
        
        path = "Scenarios/Liste_Entreprises/Liste_Ent"
        entreprises = f.getList(path, scenario)
            
        i = 0
        while i < len(bases) and len(entreprises) > 0:
            best_base = bases[i]
            basepath = "Bases/"+best_base.getFilename()
            
            new_entreprises = []
            for entreprise in entreprises:
                if not f.isEntrepriseInBase(entreprise, basepath):
                    new_entreprises.append(entreprise)
                    
            if len(new_entreprises) != len(entreprises):
                self.bases.append(best_base.getFilename())
                self.cost += best_base.getCost()
            
            entreprises = list.copy(new_entreprises)
            i+=1