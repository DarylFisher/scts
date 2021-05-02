# Defines the Entity Librry and sets initial values 

import json


class MappingField():
    def __init__(self,f,t,r):
        self.fromColumn = f
        self.toColumn = t 
        self.transformName = r

class MappingFunction(): 
    def __init__(self,f,n):
        self.fromColumns = []
        self.toColumns = []
        self.functionName = f
        self.mappingFunctionName = n

    def addFromColumn(self,c):
        self.fromColumns.append(c)

    def addToColumn(self,c):
        self.toColumns.append(c)

class MappingDefault():
    def __init__(self,c,v):
        self.columnName = c
        self.defaultValue = v

class Mapping(): 
    def __init__(self,n): 
        self.name = n
        self.mappingFields = []
        self.mappingFunctions = [] 
        self.mappingDefaults = []

    def addMappingField(self,fm):
        self.mappingFields.append(fm)
    def addMappingFunction(self,fm):
        self.mappingFunctions.append(fm)    
    def addMappingDefault(self,md):
        self.mappingDefaults.append(md) 






class MappingLibrary():
    def __init__(self):
        self.mappings = []

    def addMapping(self,m):
        self.mappings.append(m)

    def loadMapping(self,fname):
        with open(fname) as f:
            data = json.load(f)
            for mj in data["Mappings"]:
                mo = Mapping(mj["Name"])
                for pj in mj["Field Maps"]:
                    q = MappingField(pj["From"],pj["To"],pj["Transform"])
                    mo.addMappingField(q)

                for fj in mj["Functions"]:
                    q = MappingFunction(fj["Name"],fj["Function"])
                    for g in fj["FromFields"]: 
                        q.addFromColumn(g)
                    for g in fj["ToFields"]:
                        q.addToColumn(g)
                    mo.addMappingFunction(q)

                for dj in mj["Defaults"]:
                    q = MappingDefault(dj["Column"],dj["Value"])
                    mo.addMappingDefault(q)

                self.addMapping(mo)

    def dumpLibrary(self,f):
        for m in self.mappings:
            print("Mapping =" , m.name)
            print ("Fields")
            for c in m.mappingFields:
                print("  From = ", c.fromColumn, " To = ", c.toColumn, "Transform = ",c.transformName)
            
            for c in m.mappingFunctions:
                print("  Function = ", c.functionName, " Name = ", c.mappingFunctionName)

            for d in m.mappingDefaults:
                print("  Column = ", d.columnName, " Default = ", d.defaultValue)

                


def loadMappings():
    e = MappingLibrary()
    e.loadMapping("ActMap1.json")
    e.dumpLibrary("t")



loadMappings()
