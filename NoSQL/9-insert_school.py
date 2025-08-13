#!/usr/bin/env python3
"""
Module for inserting a new document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        **kwargs: Key-value pairs representing the fields of the document to insert.

    Returns:
        ObjectId: The ID of the inserted document.

    Example:
        new_id = insert_school(my_collection, name="Holberton School", address="972 Mission Street")
    """
    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
