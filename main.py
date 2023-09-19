from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values

import openai

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

# Generate embedding to request
openai.api_key = config['OPENAI_API_KEY']

model_id = "text-embedding-ada-002"
embedding = openai.Embedding.create(input="ninja", model=model_id)['data'][0]['embedding']

database_name = "legoflix"
collection_name = "sets"
db = client[database_name]
collection = db[collection_name]

similarities = collection.aggregate([
  {
    "$search": {
        "index":"default",
      "knnBeta": {
        "vector": embedding,
        "path": "embeddings_lego",
        # limit the result set
        "k": 10
      }
    }
  },
{
    "$project":{
        "embedding":0,
        "_id":0,
        'score': {
            '$meta': 'searchScore'
        }
    }
}
])

results = list(similarities)
print(results)
