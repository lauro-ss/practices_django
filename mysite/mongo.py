
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Conexão local do MongoDB
uri = "mongodb://localhost:27017"

# Se desejar conectar ao MongoDB na Nuvem altere aqui 
#uri = "mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority"


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


mongo_db = client.test

