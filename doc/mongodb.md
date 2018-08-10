# About MongoDB

MongoDB is an open-source document database that provides high performance, high availability, and automatic scaling.

## Installation
- On MacOS
```
brew update
brew install mongodb
sudo mkdir -p /data/db
sudo chown -R `id -un` /data/db
```

## Run MongoDB
- To have launchd start mongodb now and restart at login
```
brew services start mongodb
brew services stop mongodb
brew services list
```
- don't want a backgroud service
```
mongod --config /usr/local/etc/mongod.conf &
```

## Databases
- Select a database to use
```
use myDB
```

- Create a Database
If a database does not exists, MongoDB creates the database when you first store data for that database
```
use myNewDB
db.myNewCollection1.insertOne( {x: 1} )
```

## Collections

- Create
If a collection does not exist, MongoDB creates the collection when you first store data for that collection
```
db.myNewCollection2.insertOne( {x: 1} )
db.myNewCollection3.createIndex( {y:1} )
```

- Explicit Creation
db.createCollection() 

- Document validation rules

- Modifying Document Structure
update the documents to the new structure

- Unique Identifiers
Collections are assigned an immutable UUID. The collection UUID remains the same across all members of a replica set and shards in a sharded cluster.
```
db.getCollectionInfos()
```

## Views

### Create View
```
db.runCommand( { create: <view>, viewOn: <source>, pipeline: <pipeline> } )
```

```
db.runCommand( { create: <view>, viewOn: <source>, pipeline: <pipeline>, collation: <collation> } )
```

```
db.createView(<view>, <source>, <pipeline>, <collation> )
```

- The following read operations can support views
```
db.collection.find()
db.collection.findOne()
db.collection.aggregate()
db.collection.count()
db.collection.distinct()
```

## Capped Collections
Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order. Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection

See createCollection() or create for more information on creating capped collections.


## Documents

### Document Structure
```
{
   field1: value1,
   field2: value2,
   field3: value3,
   ...
   fieldN: valueN
}
```

```
var mydoc = {
               _id: ObjectId("5099803df3f4948bd2f98391"),
               name: { first: "Alan", last: "Turing" },
               birth: new Date('Jun 23, 1912'),
               death: new Date('Jun 07, 1954'),
               contribs: [ "Turing machine", "Turing test", "Turingery" ],
               views : NumberLong(1250000)
            }
```

### Embedded Documents
```
{
   ...
   name: { first: "Alan", last: "Turing" },
   contact: { phone: { type: "cell", number: "111-222-3333" } },
   ...
}
```

### Document Limitations
- The maximum BSON document size is 16 megabytes.
- To store documents larger than the maximum size, MongoDB provides the GridFS API
- _id field asts as a primary key. If an inserted document omits the _id field, the MongoDB driver automatically generates an ObjectId for the _id field.

## Shell methods
### Create a user
- db.createUser()

### Show database list
```
show dbs
```

### Show collections list
```
show collections
```

### Show the structure of the collection
```
show <collection name>
```

## Utilities

### mongodump

### mongorestore

## Client
- MongoHub
- Studio 3T or Robo 3T
