from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import db

class CtsActivity(db.Model):
    __tablename__ = 'CTS_ACTIVTY'
    ACT_ID = db.Column(db.INTEGER,nullable=False, primary_key=True )
    CPY_CD = db.Column(db.String(30),  nullable=False)
    SITE = db.Column(db.String(30),  nullable=False)
    ACT_DATE = db.Column(db.Date,  nullable=False)
    ACT_TYPE = db.Column(db.String(30),  nullable=False)
    ACT_SUB_TYPE = db.Column(db.String(30))
    EMP_CODE1 = db.Column(db.String(30),  nullable=False)
    EMP_CODE2 = db.Column(db.String(30),  nullable=False)
    EMP_CODE3 = db.Column(db.String(30),  nullable=False)
    EQP_CODE1 = db.Column(db.String(30),  nullable=False)
    EQP_CODE2 = db.Column(db.String(30))
    EQP_CODE3 = db.Column(db.String(30))
    LOC_CODE = db.Column(db.String(30))
    LOC_AREA = db.Column(db.String(30))
    CUST_GRP1 = db.Column(db.String(30),  nullable=False)
    CUST_GRP2 = db.Column(db.String(30))
    CUST_GRP3 = db.Column(db.String(30))
    PROD_GRP1 = db.Column(db.String(30),  nullable=False)
    PROD_GRP2 = db.Column(db.String(30))
    PROD_GRP3 = db.Column(db.String(30))
    ACT_REF_ID1 = db.Column(db.String(30))
    ACT_REF_ID2 = db.Column(db.String(30))
    ACT_REF_ID3 = db.Column(db.String(30))
    ACT_FACT1 = db.Column(db.NUMERIC)
    ACT_FACT2 = db.Column(db.NUMERIC)
    ACT_FACT3 = db.Column(db.NUMERIC)
    ACT_FACT4 = db.Column(db.NUMERIC)
    ACT_FACT5 = db.Column(db.NUMERIC)
    ACT_FACT6 = db.Column(db.NUMERIC)
    ACT_FACT7 = db.Column(db.NUMERIC)
    ACT_FACT8 = db.Column(db.NUMERIC)
    ACT_FACT9 = db.Column(db.NUMERIC)
    ACT_FACT0 = db.Column(db.NUMERIC)
    CREATE_DATE = db.Column(db.Date,  nullable=False)
    CREATE_TRAN = db.Column(db.String(30))
    
class CtsActivityType(db.Model):
    __tablename__ = 'CTS_ACTIVTY_TYPE'
    ACT_TYPE_ID = db.Column(db.INTEGER,nullable=False, primary_key=True )
    CPY_CD = db.Column(db.String(30),  nullable=False)
    ACT_TYPE = db.Column(db.String(30),  nullable=False)
    ACT_NAME = db.Column(db.String(100),  nullable=False)
    ACT_REF_ID1_NAME = db.Column(db.String(100),  nullable=False)
    ACT_REF_ID2_NAME = db.Column(db.String(100),  nullable=False)
    ACT_REF_ID3_NAME = db.Column(db.String(100),  nullable=False)
    ACT_FACT1_FACTOR = db.Column(db.INTEGER,nullable=False)
    ACT_FACT2_FACTOR = db.Column(db.INTEGER)
    ACT_FACT3_FACTOR = db.Column(db.INTEGER)
    ACT_FACT4_FACTOR = db.Column(db.INTEGER)
    ACT_FACT5_FACTOR = db.Column(db.INTEGER)
    ACT_FACT6_FACTOR = db.Column(db.INTEGER)
    ACT_FACT7_FACTOR = db.Column(db.INTEGER)
    ACT_FACT8_FACTOR = db.Column(db.INTEGER)
    ACT_FACT9_FACTOR = db.Column(db.INTEGER)
    ACT_FACT0_FACTOR = db.Column(db.INTEGER)
    
class CtsMODEL(db.Model):
    __tablename__ = 'CTS_MODEL'
    MODEl_ID = db.Column(db.INTEGER,nullable=False, primary_key=True )
    CPY_CD = db.Column(db.String(30),  nullable=False)
    MOD_NAME = db.Column(db.String(30),  nullable=False)
    MOD_STATUS = db.Column(db.String(100),  nullable=False)


class CtsCOMPONENET(db.MODEL):
    __tablename__ = 'CTS_MODEL'
    COMPONENT_ID = db.Column(db.INTEGER,nullable=False, primary_key=True )
    CPY_CD = db.Column(db.String(30),  nullable=False)
    MODEL_ID = db.Column(db.INTEGER,  nullable=False)
    COMPONENT_NAME = db.Column(db.String(100),  nullable=False)
    

class CtsFunction(db.Model):
    __tablename__ = 'CTS_FUNCTION'
    FUNCTION_ID = db.Column(db.INTEGER,nullable=False, primary_key=True )
    CPY_CD = db.Column(db.String(30),  nullable=False)
    FUNCTION_TYPE = db.Column(db.String(30),  nullable=False)
    ACT_DEFN_ID = = db.Column(db.INTEGER,nullable=False)
    
class CfsFactor(db.Model):
    __tablename__ = 'CTS_FACTOR'    
    FACTOR_ID = db.Column(db.INTEGER,nullable=False, primary_key=True )
    CPY_CD = db.Column(db.String(30),  nullable=False)
    FACTOR_NAME = db.Column(db.String(30),  nullable=False)
    
    
class CtsCosts(db.Model):
    __tablename__ = 'CTS_COSTS'    
    COST_ID = = db.Column(db.INTEGER,nullable=False, primary_key=True )
    CPY_CD = db.Column(db.String(30),  nullable=False)
    COST_NAME = db.Column(db.String(30),  nullable=False)
       
    
    
    