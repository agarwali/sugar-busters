from peewee import *
import os
from datetime import datetime, timedelta

# Create a database
from app.config import load_config
from playhouse.shortcuts import model_to_dict, dict_to_model


dynamicDB = MySQLDatabase("sugar_busters", host=os.getenv('IP'), user=os.getenv('C9_USER'), passwd="")


class DynamicModel (Model):
  class Meta:
    database = dynamicDB
  
######################################################
# DYNAMIC MODELS
######################################################
    
class Physician (DynamicModel):
  pId           = PrimaryKeyField()
  pName         = CharField()
  pAddress      = CharField()
  pCity         = CharField()
  pState        = CharField()
  pZip          = IntegerField()

class User (DynamicModel):
  uId           = PrimaryKeyField()
  pwrd          = CharField(null = False)
  fName         = CharField()
  lName         = CharField()
  memberId      = CharField()
  dob           = DateTimeField()
  effectiveDate = DateTimeField()
  telephone     = CharField()
  physician     = ForeignKeyField(Physician)
  lastChecked   = DateTimeField()
  profilePic    = CharField(null=True)
  period        = DateTimeField()
  

class Relationship (DynamicModel):
  rId           = PrimaryKeyField()
  f1            = ForeignKeyField(User, related_name='f1_f2')
  f2            = ForeignKeyField(User, related_name='f2_f1')
  relationtype  = CharField()