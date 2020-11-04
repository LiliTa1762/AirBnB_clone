#!/usr/bin/python3
"""
Class with the cities attributes
"""


from models.base_model import BaseModel


class State(BaseModel):
    """State class

    Args:
        BaseModel ([state]): [name]
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Contructor"""
        super().__init__(*args, **kwargs)
