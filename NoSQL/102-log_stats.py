#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs with top IPs.
"""
from pymongo import MongoClient


def log_stats():
    """
    Display stats about Nginx logs in MongoDB including top 10 IPs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = logs_collection.aggregate(pipeline)
    for ip_doc in top_ips:
        print(f"\t{ip_doc['_id']}: {ip_doc['count']}")


if __name__ == "__main__":
    log_stats()
