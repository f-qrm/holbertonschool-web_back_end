#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
        list: A list of dictionaries representing all documents in the collection.
              Returns an empty list if the collection is None or empty.
    
    Example:
        documents = list_all(my_collection)
    """
    if mongo_collection is None:
        return []
    documents = list(mongo_collection.find())
    return documents
