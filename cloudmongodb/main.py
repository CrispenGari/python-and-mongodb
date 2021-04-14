import pymongo
password ="YOUR_PASSWORD"
databaseName = "customers"
connection_url = f'mongodb+srv://crispen:{password}@cluster0.zzr2y.mongodb.net/{databaseName}?retryWrites=true&w=majority'
client = pymongo.MongoClient(connection_url)


db = client.blob
print(db.collection_names())
cursor = db.customers.find({}).sort("name", 1)
for doc in cursor:
    print(doc)


