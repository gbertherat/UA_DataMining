from Node import Node
import file as f
import copy

def buildTree(scenario):
    root = Node([], 0, [])
    
    bases = f.getAllBasesInScenario(scenario)
    sorted_bases = sorted(bases, key=lambda x: x.getCost(), reverse=True) 
    
    path = "Scenarios/Liste_Entreprises/Liste_Ent"
    etpScenario = f.getList(path, scenario)
    
    curParent = root
    for base in sorted_bases:
        child_node = Node(copy.deepcopy(curParent.getEntreprises()), 
                         curParent.getCost(), 
                         [])
        
        for entreprise in etpScenario:
            if entreprise not in child_node.getEntreprises() and f.isEntrepriseInBase(entreprise, base.getFilename()):
                child_node.addEntreprise(entreprise)
                
                if root.getCost() == child_node.getCost():
                    child_node.setCost(child_node.getCost() + f.getBaseCost(base))
                    
        curParent.addChild(child_node)
        curParent = child_node