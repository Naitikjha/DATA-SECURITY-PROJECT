from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

uri = os.getenv("MONGO_DB_URL")

client = MongoClient(
    uri,
    server_api=ServerApi('1'),
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000
)

try:
    client.admin.command("ping")
    print(" MongoDB connection successful")
except Exception as e:
    print(" MongoDB connection failed")
    print(e)

