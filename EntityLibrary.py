# Defines the Entity Librry and sets initial values 
from EntityMagic import EntityDefinition
from EntityMagic import ColumnDefinition
import json

class EntityLibrary():
    def __init__(self):
        self.entities = []

    def addEntity(self,e):
        self.entities.append(e)

    def loadEntity(self,fname):
        with open(fname) as f:
            data = json.load(f)
            for ej in data["Entity"]:
                eo = EntityDefinition(ej["Name"])
                for cj in ej["Columns"]:
                    co = ColumnDefinition(cj["Column"],cj["Data Type"])
                    eo.addColumn(co)
                self.addEntity(eo)

    def dumpLibrary(self,f):
        for e in self.entities:
            print("Entity =" , e.entityName)
            for c in e.columns:
                print("  Column = ", c.columnName, " Type = ", c.dataType )




def loadLibrary():
    e = EntityLibrary()
    e.loadEntity("Entities.json")
    e.dumpLibrary("t")



loadLibrary()
