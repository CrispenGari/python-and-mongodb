## Python + MongoDb
* this is a quick walk through python working with mongoD

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=pymongo&color=orange"/>
<img src="https://img.shields.io/static/v1?label=database&message=mongodb&color=green"/>
</p>
<p align="center">
<img align="center" src="https://i.morioh.com/2020/02/24/a220d7ff8d12.jpg" alt="py+mongo"/>
</p>

### Setup
1. First you need to download and install [MongoDB database](https://www.mongodb.com/)
2. Install pymongo
   * to install pymongo run the command
   ````shell
   pip install pymongo
   ````

### Connecting to the Database
To connect to mongodb it is simple as doing the following:
```
import pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
```
OR 
```
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
```
### Creating a database
> In mongoDB a database is only created if and only if it has contents in it:
* Creating a new database in mongoDb is simple as doing the following

```
import pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
db = client["shop"]
```
### Listing Created Database
* To list all created database using pymongo we do it as follows
```
print(client.list_database_names())
```

### Creating a collection
> Just like creating a database a collection will be created if and only if it contains some contents in it.

* Let's create a collection `customers` in our database.

### Listing the collections that are in the database:
* To lists all the collections that are in the database we do it as follows:
```
print(db.collection_names())
```

### Inserting Documents in a collection
* To insert documents in the collection we use the following methods:
    1. `insert_one()`
    2. `insert_many()`
    
#### 1. `insert_one()`
* This method insert one document in the collection name example:
```
import pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
db = client["shop"]
customers = db["customers"]
customer ={
    "name":"customer1",
}
cursor = customers.insert_one(customer)
print("Inserted", cursor.inserted_id)
```
#### 2. `insert_many()`
* This method insert multiple documents in the collection:

```
import pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
db = client["shop"]
customers = db["customers"]
customersInfo =[
    {"name":"customer3"}, {"name":"customer100"}
]
cursor = customers.insert_many(customersInfo)
print(cursor.inserted_ids)
```

### Finding the docs
* There are two methods in mongoDB that are used to query documents from a collection which are:
    1. `find()`
    2. `findOne()`


#### 1. `findOne()`
* used to get a single document that occurs first in a collection
```
cursor = customers.find_one({"name":"customer3"})
print(cursor)
```
#### 1. `find()`
* get all the documents that meet a certain condition:
```
cursor = customers.find({"name":"customer3"})
for doc in cursor:
    print(doc)
```
> Listing all the docs in the collection:

```
cursor = customers.find({})
for doc in cursor:
    print(doc)
```

### Sotting documents
* In mongoDb the `sort()` method is used to sort the documents. For example let's sort our documents base on name:

#### Ascending order
```
cursor = customers.find().sort("name")
for doc in cursor:
    print(doc)
OR
cursor = customers.find().sort("name", 1)
for doc in cursor:
    print(doc)
```
#### Descending Order
```
cursor = customers.find().sort("name", -1)
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
cursor = customers.delete_one({"name": "customer100"})
print(cursor.raw_result)
```
#### 1. `delete_many()`
* To delete many document we use the `delete_many()` method the following is an example on how to delete a documents that matches a condition:
```
cursor = customers.delete_many({"name": "customer3"})
print(cursor.raw_result)
```

### Dropping a collection
* Dropping a collection means deleting a collection from a database. Let's delete our collection `customers`
```
cursor = customers.drop()
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
cursor = customers.update_one({"name": "Name1"}, {"$set": {"name": "Name100"}})
print(cursor.raw_result, cursor.modified_count)
```

#### 2. `update_many()`
* to update all collections that matches a query we do it as follows:
```
cursor = customers.update_one({"name": "Name2"}, {"$set": {"name": "Name200"}})
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
cursor = customers.find().limit(5)
for doc in cursor:
    print(doc)
```
> That's the basics about python + mongodb using `pymongo`

### Credits:
* [w3schools](https://www.w3schools.com/python/python_reference.asp)
* [pymongo](https://pymongo.readthedocs.io/en/stable/)



