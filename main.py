import file as f

from BranchAndBound import BranchAndBound
from Glouton import Glouton


def main():    
    for scenario in range(1, 4):
        print("\n-----------")
        print("Scenario n°" + str(scenario))
        
        # Test Glouton
        print("-----------")
        print("Glouton: ")
        
        glouton = Glouton()
        glouton.start(scenario)
        print("Cost: " + str(glouton.cost))
        print("Bases: " + str(glouton.bases))
        
        # Test B&B
        print("-----------")
        print("Branch And Bound: ")
        BandB = BranchAndBound()
        bases = sorted(f.getAllBasesInScenario(scenario), key=lambda x: x.getRatio(), reverse=True)
        cost = BandB.start(scenario)
        
        print("Cost: " + str(cost))
        print("[", end="")
        for i, base in enumerate(BandB.bases):
            if base:
                print('\'' + bases[i].getFilename(), end="' ")
        print("]")
        print("")
            
    
if __name__ == "__main__":
    main()