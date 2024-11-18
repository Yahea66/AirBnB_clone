#!/usr/bin/python3
"""
This module defines the FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
import os


class FileStorage:
    """
    A FileStorage class for serializing and deserializing Python objects to and from a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary that stores all objects with key as '<class name>.<id>'.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary containing all stored objects.

        Returns:
            dict: The dictionary of all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj (object): The object to be stored, must have 'id' and '__class__.__name__' attributes.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the __objects to the JSON file specified by __file_path.
        """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists, otherwise does nothing.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            FileStorage.__objects.clear()
            for key, obj_data in objs.items():
                cls_name = key.split('.')[0]
                if cls_name in globals():
                    cls = globals()[cls_name]
                    obj = cls.from_dict(obj_data)
                    FileStorage.__objects[key] = obj
