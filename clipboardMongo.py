import pymongo
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def findWord(word):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	try:
		mydb = myclient["VocabWord"]
		mycol = mydb["Words"]
		x = mycol.find({"VocabWord":word}).count()
		# print(x)
		if x!=0:
			return True
		else:
			return False 
	except:
		print('An error occurred.')


def jsonToMongo(jsonDict):
	# try:
		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		mydb = myclient["VocabWord"]
		mycol = mydb["Words"]
		if(findWord(jsonDict["VocabWord"])):
			# print("repeat")
			mycol.find_one_and_update({ 'VocabWord':jsonDict["VocabWord"]}, {'$inc':{'OccurrenceCount': 1 }} )

		else:
			# mycol.insert(json.dumps(jsonDict, cls=JSONEncoder))
			jsonDict['OccurrenceCount']=0
			# print("Here ",jsonDict)
			mycol.insert(jsonDict)
			print("no repeat")
	# except:
	# 	print('An error occurred.')
		return