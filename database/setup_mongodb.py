
from pymongo import MongoClient

import pandas as pd

uri = "mongodb://unlimiteddemi:Kmyh4MSII9tHbbIK@cluster0.ddje26o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client['candidate_db']
profiles_collection = db['profiles']
resumes_collection = db['resumes']

# Insert candidate profiles
profiles_df = pd.read_csv('C:/Users/USER/Documents/Projects/Profile_matching/data/candidate_data.csv')
profiles_collection.insert_many(profiles_df.to_dict('records'))
profiles_collection.create_index([("Job Skills", "text")])

# Insert resumes
resumes_df = pd.read_csv('C:/Users/USER/Documents/Projects/Profile_matching/data/Resume.csv')
resumes_collection.insert_many(resumes_df.to_dict('records'))

print("MongoDB setup complete.")


if profiles_collection:
    print("Connected to profile")
