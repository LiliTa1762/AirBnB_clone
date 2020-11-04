#!/usr/bin/python3
"""
Class with the user attributes
"""

from .base_model import BaseModel


class User(BaseModel):
    """User class

    Args:
        Ex: BaseModel ([user]): [email]
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Method init"""
        super().__init__(*args, **kwargs)
