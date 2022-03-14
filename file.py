import os

from Base import Base
           
def getList(path, i):
    if path == "" or i == None :
        return None

    names = []
    if(os.path.isfile(path + str(i) + '.txt')):
        with open(path + str(i) + '.txt', 'r') as file:
            i = 0
            for i, line in enumerate(file):
                if i > 0:
                    line = line.replace("\n","")
                    if(line != ''):
                        names.append(line.replace("\n",""))
    return names

def getAllBases():
    path = "Bases/"
    
    files = []
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            files.append(filename)
    return files

def getAllBasesInScenario(i):
    bases = []
    path = 'Scenarios/Liste_Bases/Liste_Bases'     
    
    for basename in getList(path, i):
        cost = getBaseCost(basename)
        entreprises = getBaseContent(basename)
        
        base = Base(basename, cost, entreprises)
        bases.append(base)
        
    return bases


def getBaseCost(base):
    if(base == ""):
        return None
    
    path = 'Bases/'
    
    if(os.path.isfile(path + base)):
        with open(path + base, 'r') as file:
            return int(file.readline().replace("\n",""))

def getBaseContent(base):
    if(base == ""):
        return None
    
    path = 'Bases/'
    
    names = []
    if(os.path.isfile(path + base)):
        with open(path + base, 'r') as file:
            for i, line in enumerate(file):
                if(i > 1):
                    names.append(line.replace('\n',''))
    return names
            
def isEntrepriseInBase(entreprise, base):
    if(os.path.isfile(base)):
        with open(base, 'r') as file:
            for i, line in enumerate(file):
                if i > 1:
                    if line.replace('\n','') == entreprise:
                        return True
    return False