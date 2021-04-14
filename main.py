
import pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
db = client["shop"]
customers = db["customers"]

cursor = customers.find().limit(5)
for doc in cursor:
    print(doc)
