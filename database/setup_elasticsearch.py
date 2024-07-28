import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch(
    "https://a219db0c9a52430d82ebb7ad71ed5b02.us-central1.gcp.cloud.es.io:443",
    api_key="X1o2eThwQUJyZHhtemJ2SS1RTVM6NGo1c0NCMTJRZUNzQlh4QUlyZVJrZw=="
)


csv_file_path = 'C:/Users/USER/Documents/Projects/Profile_matching/data/candidate_data.csv'  
df = pd.read_csv(csv_file_path)


index_name = 'candidates'


def upload_document(row):
    document = row.to_dict()
    response = es.index(index=index_name, document=document)
    return response


for index, row in df.iterrows():
    upload_document(row)

print("Data upload complete.")
