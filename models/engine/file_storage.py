"""
This module provides the FileStorage class for handling serialization and
deserialization of Python objects to and from JSON format. It is designed to
allow easy storage and retrieval of persistent objects across sessions.

The FileStorage class uses a dictionary to keep track of objects and saves/loads
them to/from a JSON file specified by a path. This mechanism supports basic
ORM-like functionality for Python classes that implement a  method
and can be initialized with keyword arguments.
"""

class FileStorage:
    """
    A class for handling the storage of objects in a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary to store objects with keys in the format
                          "<class_name>.<object_id>".

    Methods:
        all(): Returns the dictionary containing all stored objects.
        new(obj): Adds an object to the storage dictionary.
        save(): Serializes the objects in the storage dictionary to a JSON file.
        reload(): Deserializes objects from the JSON file and loads them into the storage dictionary.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve the dictionary of all objects currently stored.

        Returns:
            dict: A dictionary containing all objects stored in the FileStorage instance.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Parameters:
            obj (object): The object to be stored, which must have 'id' attribute and belong to a class
                          with a  attribute.

        No return value. The object is added to the __objects dictionary with its class name and id
        as the key in the format "<class_name>.<object_id>".
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the storage dictionary to a JSON file specified by __file_path.

        This method iterates over the __objects dictionary and calls the  method
        on each object to convert it to a dictionary, which is then serialized to JSON.

        No return value. The content is written to the file specified by __file_path.
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        Deserializes objects from the JSON file specified by __file_path and restores them
        into the storage dictionary.

        This method checks if the file exists, reads the JSON content, and then reconstructs
        the objects based on their class name and attributes stored in JSON. The objects are
        then added back into the __objects dictionary.

        No return value. Objects are restored into the __objects dictionary.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for key, val in objs.items():
                cls_name = key.split('.')[0]
                cls = globals()[cls_name]
                obj = cls(**val)
                FileStorage.__objects[key] = obj
