## Python + Cloud MongoDB
In this one we are going to connect cloud mongodb with python.

<p align="center">
<img  src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=pymongo&color=orange"/>
<img src="https://img.shields.io/static/v1?label=database&message=mongodb&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=dnspython&color=purple"/>
</p>
<p align="center">
<img width="60%" align="center" src="https://i.morioh.com/2020/02/24/a220d7ff8d12.jpg" alt="py+mongo"/>
</p>
### Setup
We need to install two packages which are:
    1. `pymongo`
    2. `dnspython`
To install these run the following commands:
````shell
pip install dnspython
pip install pymongo
````

### Then
* Go to [MongoDB](https://cloud.mongodb.com/v2/) create an account or login if you already have an existing one:
* The instructions on how to create a cluster can be found [Here](https://blog.pythonanywhere.com/178/)
* after everything is seted up in the cloud now we can work with python code

### Connecting
* We need a connection string that will be found during creation of the cluster.
* We also need a password which will be found during setup as well
```
import pymongo
password ="YOUR_PASSWORD"
databaseName = "customers"
connection_url = f'mongodb+srv://crispen:{password}@cluster0.zzr2y.mongodb.net/{databaseName}?retryWrites=true&w=majority'
client = pymongo.MongoClient(connection_url)
cursor = client.list_database_names()
print(cursor)
```


### Inserting Documents in a collection
* To insert documents in the collection we use the following methods:
    1. `insert_one()`
    2. `insert_many()`
    
#### 1. `insert_one()`
* This method insert one document in the collection name example:
```
db = client.blob
cursor = db.customers.insert_one({"name":"name1"})
print("Inserted", cursor.inserted_id)
```
#### 2. `insert_many()`
* This method insert multiple documents in the collection:

```
db = client.blob
customersInfo = [
    {"name":"customer3"}, {"name": "customer100"}
]
cursor = db.customers.insert_many(customersInfo)
print("Inserted", cursor.inserted_ids)
```

### Finding the docs
* There are two methods in mongoDB that are used to query documents from a collection which are:
    1. `find()`
    2. `findOne()`


#### 1. `findOne()`
* used to get a single document that occurs first in a collection
```
cursor = db.customers.find_one({"name":"customer3"})
print(cursor)
```
#### 1. `find()`
* get all the documents that meet a certain condition:
```
db = client.blob
cursor = db.customers.find({"name":"customer3"})
for doc in cursor:
    print(doc)
```
> Listing all the docs in the collection:

```
db = client.blob
cursor = db.customers.find({})
for doc in cursor:
    print(doc)
```

### Sorting documents
* In mongoDb the `sort()` method is used to sort the documents. For example let's sort our documents base on name:

#### Ascending order
```
db = client.blob
cursor = db.customers.find().sort("name")
for doc in cursor:
    print(doc)
OR
cursor = db.customers.find().sort("name", 1)
for doc in cursor:
    print(doc)
```
#### Descending Order
```
db = client.blob
cursor = db.customers.find().sort("name", -1)
for doc in cursor:
    print(doc)
```

### Deleting documents
* To delete documents we use the following methods:
    1. `delete_one()`
    2. `delete_many()`
    
#### 1. `delete_one()`
* To delete one document we use the `delete_one()` method the following is an example on how to delete a document that matches a condition:
```
db = client.blob
cursor = db.customers.delete_one({"name": "customer100"})
print(cursor.raw_result)
```
#### 1. `delete_many()`
* To delete many document we use the `delete_many()` method the following is an example on how to delete a documents that matches a condition:
```
db = client.blob
cursor = db.customers.delete_many({"name": "customer3"})
print(cursor.raw_result)
```

### Dropping a collection
* Dropping a collection means deleting a collection from a database. Let's delete our collection `customers`
```
db = client.blob
cursor = db.customers.drop()
print(db.collection_names()) # []
print("Collection deleted")
```
### Updating Collection
* To update a collection we use one of the methods which are:
    1. `update_one()`
    2. `update_many()`
    
    
#### 1. `update_one()`
* to update a single collection that matches a query we do it as follows:
```
db = client.blob
cursor = db.customers.update_one({"name": "Name1"}, {"$set": {"name": "Name100"}})
print(cursor.raw_result, cursor.modified_count)
```

#### 2. `update_many()`
* to update all collections that matches a query we do it as follows:
```
db = client.blob
cursor = db.customers.update_one({"name": "Name2"}, {"$set": {"name": "Name200"}})
print(cursor.raw_result, cursor.modified_count)
```

### Limit the Result
To limit the results we use the `limit()` method which takes one parameter an integer which is the total number of documents that will be returned:
> Suppose we have the following documents in our collection and we want to get only first 5 customers we can do it as follows:
 
```
{'_id': 1, 'name': 'John', 'address': 'Highway37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
```
#### `code`:
```
db = client.blob
cursor = db.customers.find().limit(5)
for doc in cursor:
    print(doc)
```
> That's the basics about python + cloud mongodb using `pymongo`










