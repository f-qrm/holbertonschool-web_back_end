#!/usr/bin/env python3
"""
Module for updating documents in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the 'topics' field of all documents with a given name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        name (str): The value of the 'name' field to match documents.
        topics (list): A list of topics to set for the matched documents.

    Returns:
        dict: The result of the update operation, containing information like
              the number of documents matched and modified.

    Example:
        update_topics(my_collection, "Holberton School", ["Python", "JavaScript"])
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics} }
    )
