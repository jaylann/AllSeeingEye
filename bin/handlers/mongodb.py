from pymongo import MongoClient

class AllSeeingEye:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(AllSeeingEye, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_url='mongodb://localhost:27017/', db_name='AllSeeingEye'):
        if self._initialized:
            return
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self._initialized = True

    def insert_one(self, collection_name, data):
        """ Insert a document into a collection """
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id

    def find(self, collection_name, query):
        """ Find documents from a collection """
        collection = self.db[collection_name]
        return collection.find(query)

    def delete_one(self, collection_name, query):
        """ Delete a document from a collection """
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count

    @classmethod
    def reset_singleton(cls):
        """ Reset the singleton instance. """
        cls._instance = None
