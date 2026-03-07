#!/usr/bin/env python3
"""
Module that provides a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents, or empty list if no documents exist
    """
    return list(mongo_collection.find())
