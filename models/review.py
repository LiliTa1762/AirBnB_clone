#!/usr/bin/python3
"""
Class with the reviews attributes
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class

    Args:
        Ex: BaseModel ([review]): [text]
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Built method"""
        super().__init__(*args, **kwargs)
