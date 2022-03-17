from numpy import math
import file as f
import math
import Tree 

def branch_bound(scenario):

    bases = f.getAllBasesInScenario(scenario)
    sorted_bases = sorted(bases, key=lambda x: x.getRatio(), reverse=True)
    
    path = "Scenarios/Liste_Entreprises/Liste_Ent"
    entreprises = f.getList(path, scenario)

    upper_bound = math.inf
    lower_bound = 0
    current_best = None



    