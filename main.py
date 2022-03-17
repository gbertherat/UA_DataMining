
from branch_bound import branch_bound
from glouton import *

def main():
    scenario = 1
    
    # Test Glouton
    #baseGlouton = glouton(scenario)
    #print(baseGlouton["cost"])
    #print(baseGlouton["bases"])
    
    # Test B&B
    branch_bound(scenario)
    
    
if __name__ == "__main__":
    main()