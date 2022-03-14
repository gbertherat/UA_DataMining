
from glouton import *

def main():
    scenario = 1
    
    # Test Glouton
    baseGlouton = glouton(scenario)
    print(baseGlouton["cost"])
    print(baseGlouton["bases"])
    
if __name__ == "__main__":
    main()