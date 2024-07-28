from pymongo import MongoClient
import pandas as pd
from database.setup_mongodb import client

from database.setup_mongodb import db
db = client['candidate_db']
profiles_collection = db['profiles']

df = pd.read_csv('C:/Users/USER/Documents/Projects/Profile_matching/data/cleaned_candidate_data.csv')

df = df.dropna(subset=['name', 'email', 'phone', 'address'])
profiles_collection.delete_many({})

# Insert profiles into MongoDB
profiles_collection.insert_many(df.to_dict('records'))

print("Indexing complete.")
