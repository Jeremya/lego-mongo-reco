from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values

import csv

config = dotenv_values('.env')
uri = config['MONGODB_URI']

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['legoflix']
collection = db['sets']

with open('resources/sets.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)

    for row in reader:
        # Create a dictionary for the row using headers as keys
        row_dict = dict(zip(headers, row))

        # Insert the row into mongodb
        collection.insert_one(row_dict)

        print(f"Inserted set {row_dict['set_num']} into MongoDB")

