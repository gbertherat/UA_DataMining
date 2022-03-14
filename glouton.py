import file as f

def glouton(scenario):
    bases = f.getAllBasesInScenario(scenario)
    sorted_bases = sorted(bases, key=lambda x: x.getRatio(), reverse=True)
    
    path = "Scenarios/Liste_Entreprises/Liste_Ent"
    entreprises = f.getList(path, scenario)
        
    cost = 0
    found_bases = []
    
    i = 0
    while i < len(sorted_bases) and len(entreprises) > 0:
        best_base = sorted_bases[i]
        basepath = "Bases/"+best_base.getFilename()
        
        new_entreprises = []
        for entreprise in entreprises:
            if not f.isEntrepriseInBase(entreprise, basepath):
                new_entreprises.append(entreprise)
                
        if len(new_entreprises) != len(entreprises):
            found_bases.append(best_base.getFilename())
            cost += best_base.getCost()
        
        entreprises = list.copy(new_entreprises)
        i+=1
        
    return {"cost": cost, "bases": found_bases}