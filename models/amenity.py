#!/usr/bin/python3
"""
Class with the amenities attributes
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class

    Args:
        BaseModel ([amenity]): [name]
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of amenity class"""
        super().__init__(*args, **kwargs)
