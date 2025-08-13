#!/usr/bin/env python3
"""Count and display logs from the nginx collection in MongoDB."""
from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.log
    collection = db.nginx

    log_count = collection.count_documents({})
    print(f'{log_count} logs')

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELET']
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f'/tmethod {method}: {count}')

    status_check = collection.count_documents(
        {'method': 'GET', 'path': '/status'}
        )
    print(f'{status_check} status check')
