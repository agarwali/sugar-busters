#Built in libraries import
import os, sys, importlib

#Import personally created files
from app.model_files.models import *
from app.config import *
from app.everything import *

# Retreive the db path from the 
conf = load_config('app/config.yaml')

# Drops all Values in the tables
def drop_tables(table_lst):
  for table in table_lst:
    try:
      table.drop_table(True, True)
      print str(table) + " was dropped"
    except:
      print str(table) + " does not exist"
      

#Retreives all the class's from the module_name and returns them
def class_from_name (module_name, class_name):
    """Reads all class names from """
    # load the module, will raise ImportError if module cannot be loaded
    # m = __import__(module_name, globals(), locals(), class_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(module_name, class_name)
    return c

def get_classes (db):
  classes = []
  for str in conf['models'][db]:
    print ("\tRetreiveing Model for '{0}'".format(str))
    c = class_from_name(sys.modules[__name__], str)
    classes.append(c)
  return classes

# This empties the database tables
class_lst = conf["models"]["dynamic"]
drop_tables(get_classes("dynamic"))
print "It passed here"

# This uses Peewee to populate a table with all of the dynamic classes in config.yaml 
dynamicDB.create_tables(get_classes('dynamic'), safe=True)

# Populate Chemical Table with dummy data.

p1 = Physician(
    pName = "Dr. John Doe",
    pAddress = "2292 US-27 #300, Somerset",
    pCity   = "Somerset",
    pState  = "KY",
    pZip = 42501
    )
p1.save()
print "Physician table populated"
user1 = User(  
  pwrd          = "1234",
  fName         = "Ishwar",
  lName         = "Agarwal",
  memberId      = "MXXXXXXXX",
  dob           = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'),
  effectiveDate = datetime.strptime('Jun 10 2015  1:33PM', '%b %d %Y %I:%M%p'),
  telephone     = "859-XXX-XXX",
  physician     = p1.pId,
  lastChecked   = datetime.strptime('Jun 1 2016  1:33PM', '%b %d %Y %I:%M%p'),
  period        = timedelta(days=180)
  )
user1.save()
print "User table populated"
user2 = User(  
  fName         = "Xhafer",
  lName         = "Rama",
  pwrd          = "1234",
  memberId      = "MXXXXXXX",
  dob           = datetime.strptime('Jun 1 2001  1:33PM', '%b %d %Y %I:%M%p'),
  effectiveDate = datetime.strptime('Jun 10 2015  1:33PM', '%b %d %Y %I:%M%p'),
  telepone      = "859-XXX-XXX",
  physician     = p1.pId,
  lastChecked   = datetime.strptime('Jun 1 2015  1:33PM', '%b %d %Y %I:%M%p'),
  period        = timedelta(days=180)
  )
user2.save()
print "User table populated"
rel1 = Relationship(
    f1 = user1.uId,
    f2 = user2.uId,
    relationtype = "Friend"
    )
rel1.save()
rel2 = Relationship(
    f1 = user2.uId,
    f2 = user1.uId,
    relationtype = "Friend"
    )
rel2.save()
print "Relationships created"