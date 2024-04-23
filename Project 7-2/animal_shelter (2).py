from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31846
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT))
            self.database = self.client['%s' % (DB)]
            self.collection = self.database['%s' % (COL)]
            print("Connection Successful")

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  # data should be dictionary 
            return True
        else:
            #Exception
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        
    #Queries database for data and returns a Cursor containing all matching entries.
    def readAll(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("nothing to read because data parameter is empty")

    
    #Queries database for data and returns a Cursor containing the first matching entry.
    def readOne(self, data):
        if data is not None:
            return self.database.animals.find_one(data)
        else:
            raise Exception("nothing to read because data parameter is empty")
    
    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            # Handle the exception here, you can log the error message or raise a custom exception
            print(f"An error occurred during update: {e}")
            return 0  # Return 0 indicating no documents were modified

    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            # Handle the exception here, you can log the error message or raise a custom exception
            print(f"An error occurred during delete: {e}")
            return 0  # Return 0 indicating no documents were deleted