#!/usr/bin/python3
"""
This module defines the BaseModel class which serves as a base class for all other models in an AirBnB application.
It includes methods for initialization, string representation, saving, and converting object data to a dictionary.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    A base class for models in an application, providing initialization, serialization, and time tracking functionalities.
    
    Attributes can be initialized via direct assignment or from a dictionary with .
    Supports serialization to and from dictionary representation with datetime handling.
    """
  
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel either with specific attributes passed via 
        or with default values.

        Parameters:
            *args: Variable length argument list, not used in this method.
            **kwargs: Arbitrary keyword arguments containing initial values of the instance's attributes.
        """
        if kwargs:
            # Convert datetime strings to datetime objects if present
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])

            # Remove the class name entry if present, as it's not an attribute
            kwargs.pop("__class__", None)
            
            # Set attributes based on remaining items in kwargs
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            # Assign default values if no kwargs provided
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    
    def __str__(self):
        """
        String representation of the BaseModel instance, showing class name, id, and attributes.

        Returns:
            str: A formatted string representation of the instance with class name, id, and attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the  attribute to the current datetime whenever the instance is saved.
        """
        self.updated_at = datetime.now()
  
    def to_dict(self):
        """
        Serializes the instance to a dictionary which includes the class name and ISO formatted datetimes.

        Returns:
            dict: A dictionary representation of the instance, including special handling for datetime attributes
                  and the addition of the class name.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__  # Corrected typo from _class_ to __class__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
