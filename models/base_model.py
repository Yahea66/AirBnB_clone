#!/usr/bin/python3
"""
This module defines the BaseModel class which serves as a base class for all
other models in an AirBnB application.
It includes methods for initialization, string representation, saving, and
converting object data to a dictionary.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines common attributes/methods for other classes.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        Attributes:
            id (str): A unique id generated using uuid.
            created_at (datetime): A timestamp when an instance is created.
            updated_at (datetime): A timestamp for the last update which is
            identical to created_at upon creation.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Overrides the default string representation of the BaseModel instance.
        Returns:
            str: A string representation of the BaseModel instance showing the
            class name, id, and dictionary of attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute to the current time whenever an
        instance is modified.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance's attributes to a dictionary format, including
        the class name and altering the datetime attributes to be ISO formatted
        strings.

        Returns:
            dict: A dictionary containing all keys/values of __dict__ of the
            instance, with additional keys for the class name and formatted
            datetime objects.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
