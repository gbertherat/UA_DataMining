from inspect import getfile
import file as f

from BranchAndBound import BranchAndBound
from glouton import Glouton


def main():    
    for scenario in range(1, 4):
        print("\n-----------")
        print("Scenario n°" + str(scenario))
        print("-----------")
        path = "Scenarios/Liste_Entreprises/Liste_Ent"
        entreprises = f.getList(path, scenario)
        print("- Entreprises à trouver: ")
        for entreprise in entreprises:
            print("\t- " + entreprise)
        
        bases = f.getAllBasesInScenario(scenario)
        print("\n- Bases disponibles: ")
        for base in bases:
            print("\t- " + base.getFilename())
        
        # Test Glouton
        print("-----------")
        print("Glouton: ")
        
        glouton = Glouton() # Création de notre glouton
        glouton.start(scenario) # On lance l'algorithme sur le scénario
        print("Cost: " + str(glouton.cost))
        print("Bases: " + str(glouton.bases))
        
        # Test B&B
        print("-----------")
        print("Branch And Bound: ")
        BandB = BranchAndBound() # Création de notre Branch and Bound
        bases = sorted(f.getAllBasesInScenario(scenario), key=lambda x: x.getRatio(), reverse=True)
        cost = BandB.start(scenario) # On lance le branch and bound sur notre scénario
        print("Start Upperbound (par Glouton): " + str(glouton.cost))
        print("Cost: " + str(cost))
        print("Bases: [", end="")
        for i, base in enumerate(BandB.bases):
            if base:
                print('\'' + bases[i].getFilename(), end="' ")
        print("]")
        print("")
            
    
if __name__ == "__main__":
    main()