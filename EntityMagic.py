# This module performs the adding an activity function it is based on an internal activity format

class ColumnDefinition():
    def __init__(self,name,dt):
        self.columnName = name
        self.dataType = dt
        # P=Primary Key Identifier 
        # D=Date 
        # T=Time 
        # S=String
        # I=Integer
        # N=Numeric

class EntityDefinition():
    def __init__(self,t):
        self.columns = []
        self.entityName = t

    def addColumn(self,cd):
        self.columns.append(cd)


class EntityColumn():
    def __init__(self,name,value):
        self.ColumnName = name
        self.ColumnValue = value 
    def rep(self):
        print(self.ColumnName," = ", self.ColumnValue)

class BusinessEntity():
    def __init__(self,t):
        self.columns = []
        self.entityType = t
    def addColumn(self,column):
        self.columns.append(column)

class ImportEntity():
    def __init__(self):
        self.columns = []
    def addColumn(self,column):
        self.columns.append(column)
    def rep(self):
        print("Entity Rep")
        for c in self.columns:
            c.rep()

