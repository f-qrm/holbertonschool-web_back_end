#!/usr/bin/env python3
"""
Module for retrieving schools by a specific topic from a MongoDB collection.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools (documents) that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for in the 'topics' field of each document.

    Returns:
        list: A list of documents (dictionaries) that contain the given topic.

    Example:
        schools = schools_by_topic(school_collection, "Python")
    """
    if mongo_collection is None:
        return []

    documents = list(mongo_collection.find({'topics': topic}))
    return documents
