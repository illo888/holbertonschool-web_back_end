#!/usr/bin/env python3
"""
Module that provides a function to get top students sorted by average score.
"""


def top_students(mongo_collection):
    """
    Return all students sorted by average score.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of students with averageScore, sorted in descending order
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
