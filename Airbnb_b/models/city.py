#!/usr/bin/python3
"""
    A City module that inherits from BaseModel
"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """
        A City that inherits from BaseModel
    """
    state_id = "" # it will be the state.id
    name = ""