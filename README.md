# lego-python-mongo

## Description
Quick start project on Mongo DB with Python loading all Lego sets data from CSV file.

## Setup
* Create an Atlas account and cluster. 
* Create a database named `learning` and a collection named `legoflix`. 
* Create a user with read/write access to the database. 
* Create a `.env` from the template file.

To set up embeddings in Atlas, follow the instructions in [this tutorial](https://www.mongodb.com/developer/products/atlas/semantic-search-mongodb-atlas-vector-search/?hideMenu=1&lb-height=100%25&lb-width=100%25) to create a Vector Search. Add the following index.
```
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "plot_embedding": {
        "dimensions": 1536,
        "similarity": "cosine",
        "type": "knnVector"
      }
    }
  }
}
```

## Usage
* Run `python loader.py` to load the data into the database.
* Run `python main.py` to search for a lego set.