# File: base_model.py
# importing the uuid
import uuid
# importing the datetime module
from datetime import datetime
# importing the models package
import models

# Defining the BaseModel class
class BaseModel:
    """
        This class defines all commonn attributes and methods for the other classes
    """
    def __init__(self, *args, **kwargs): # using variable keyworded and non-keyworded argument
        """
            Initializing the attributes
        """
        # if kwargs is empty, we create a new instance
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4()) # generating random id
            self.created_at = datetime.now() # generating the current time
            self.updated_at = datetime.now()
        # otherwise create the keys as new attributes
        else:
            # loop through the keyworded arguments in kwargs
            for key, value in kwargs.items():
                # check if the key is created_at or updated_at
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(str(value), "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "created_at" or key != "updated_at":
                    setattr(self, key, value)


    def __str__(self): # setting the print behavior
        """
            Simulating the printing behavior
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self): # updating the attribute to the current time
        """
            updating the attribute with the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Creating the dictionary for the serialization and deserialization
        """
        new_diction = self.__dict__.copy() # copying the attri and values in dict form

        # Setting the key which is the class name
        new_diction["__class__"] = self.__class__.__name__

        # converting the two atrributes to iso format
        new_diction["created_at"] = new_diction["created_at"].isoformat()
        new_diction["updated_at"] = new_diction["updated_at"].isoformat()

        # returning the object for serialization and deserialization process
        return (new_diction)
