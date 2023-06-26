from pymongo import MongoClient
import os

MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb')
MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
common_client = MongoClient(MONGODB_URL, port=MONGODB_PORT)
common_db = common_client.test_database