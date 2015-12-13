import numpy as np
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)

db = client['dataDump']
yearArray = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
array = []
mainArray = []

for year in yearArray:
    mainArray.append(db.get_collection(year).count())
    print db.get_collection(year).count()

print np.sum(mainArray)