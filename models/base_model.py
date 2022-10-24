#!/usr/bin/python3
import uuid
import datetime
"""Module BaseModel"""


class BaseModel:
    """
    Class BaseModel that create a instance with
    attributes id, created and update
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

    def __str__(self):
        """This method return a string class"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """This method update of the instance"""
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        """
        This method modify and convert all attributes to
        string and return dictionaty
        """
        dic = self.__dict__
        dic["__class__"] = __class__.__name__
        dic["update_at"] = datetime.datetime.isoformat(self.update_at)
        dic["created_at"] = datetime.datetime.isoformat(self.created_at)
        return dic
