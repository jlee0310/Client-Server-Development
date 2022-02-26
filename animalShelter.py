from pymongo import MongoClient
from bson.objectid import ObjectId

from pymongo.message import update

class AnimalShelter(object):

    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username='aacuser', password=12345):

        # Initializing the MongoClient. This helps to

        # access the MongoDB databases and collections.

        self.client = MongoClient(port=37198)

        self.database = self.client['AAC']
        

    # The method to implement the C in CRUD.

    def create(self, data):

        if data is not None:

            self.database.animals.insert_one(data) # data should be dictionary

            print("New Animal is added-----------------")

        else:

            raise Exception("Failed to add Data")

           

    # The method to implement the R in CRUD.

    def read(self, criteria):

        if criteria is not None:

            data = self.database.animals.find(criteria) # data should be dictionary

            for document in data:

                print(document)

            return data

        else:

            raise Exception("Failed to read Data")
    
    
    # The method to implement the U in CRUD.
       
    def update(self, criteria, new_val):
        
        if criteria is not None and new_val is not None: 
            
            x = self.database.animals.update_many(criteria,{"$set":new_val})
            print(x.modified_count, " documents updated.")
            
        
        else:
            raise Exception("Nothing to update.")
            
            
    # The method to implement the D in CRUD.
    
    def delete(self, animal):
        if animal is not None:
            data = self.database.animals.delete_many(animal)
            print(data.deleted_count, " documents deleted.")
            if data is None:
                print("Animal does not exists")
             
        else:
            raise Exeption("noting to delete, animal data is empty")
    
            



           
