import math
import tree
from Node import Node

def branch_bound(scenario):
    tree.buildTree(scenario)
    
    
    #A = [Node()]
    #UB = math.inf
#
    #path = "Scenarios/Liste_Entreprises/Liste_Ent"
    #
    #currentbest = None
    #while len(A) != 0:
    #    A = sorted(A, key=lambda x: x.getCost(), reverse=True)
    #    
    #    k = A[0]
    #    A.remove(k)
    #    
    #    for i in range(1, len(k.getChildren())):
    #        if k.getCost() <= UB:
    #            if len(k.getChildren()[i]) == 0:
    #                UB = k.getChildren()[i].getCost()
    #                currentbest = k.getChildren()[i]
    #            else:
    #                A.append(k.getChildren()[i])



    