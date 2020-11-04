#!/usr/bin/python3
"""
Class with the cities attributes
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class

    Args:
        BaseModel ([city]): [state_id] [name]
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of city class"""
        super().__init__(*args, **kwargs)
