#!/usr/bin/python3
"""
A module Review that inherits from BaseModel
"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class Review that inherits from BaseModel
    """
    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""