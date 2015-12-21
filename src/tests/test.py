import json

data = {}
subData = {}
subData['data'] = [5002]
subData['name'] = 'test'

mainArray = []
mainArray.append(subData)
mainArray.append(subData)
mainArray.append(subData)
data['series'] = mainArray
json_data = json.dumps(data)

print json_data