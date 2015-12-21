from pymongo import MongoClient
import json

class ArrestCrime:

    def main_Method(self):
        client = MongoClient('localhost', 27017)
        db = client['dataDump']
        yearArray = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
        data = {}
        mainArray = []
        for year in yearArray:
            subData = {}
            subData['data'] = [db.get_collection(year).count()]
            subData['name'] = str(year)
            mainArray.append(subData)
        data['series'] = mainArray
        json_data = json.dumps(data)

        return json_data