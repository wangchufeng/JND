from pymongo import MongoClient
dbIp = 'localhost'

class DB:
    def connectDB(self, dbname, collectionname, dbip, port):
        self._conn = MongoClient(dbip, port)
        self._db = self._conn[dbname]
        self._collection = self._db[collectionname]
        return self._collection;

    def getNewId(self):
        if(self._collection.find_one({'type': 'id'}) == None):
            self._collection.insert_one({'type': 'id', 'newid': 0})
        newId = int(self._collection.find_one({'type': 'id'})['newid'])
        newId += 1
        print('newid', newId)
        self._collection.update({"type": 'id'}, {'$set': {'newid': newId}})
        return newId

    def insertATest(self, data):
        return self._collection.insert_one(data)
       