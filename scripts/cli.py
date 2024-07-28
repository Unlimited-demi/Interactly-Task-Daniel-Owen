from pymongo import MongoClient
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from elasticsearch import Elasticsearch

uri = "mongodb://unlimiteddemi:tBLzzgx35XlDQmKr@cluster0.ddje26o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(uri)
db = mongo_client['candidate_db']
profiles_collection = db['profiles']


es = Elasticsearch(
    "https://a219db0c9a52430d82ebb7ad71ed5b02.us-central1.gcp.cloud.es.io:443",
    api_key="X1o2eThwQUJyZHhtemJ2SS1RTVM6NGo1c0NCMTJRZUNzQlh4QUlyZVJrZw=="
)

tokenizer = GPT2Tokenizer.from_pretrained('C:/Users/USER/Documents/Projects/Profile_matching/models/fine_tuned_gpt2')
model = GPT2LMHeadModel.from_pretrained('C:/Users/USER/Documents/Projects/Profile_matching/models/fine_tuned_gpt2')

def retrieve_profiles_from_mongo(job_description):
   
    matching_profiles = profiles_collection.aggregate([
        {
            "$search": {
                "index": "default", 
                "text": {
                    "query": job_description,
                    "path": "Job Skills"
                }
            }
        },
        {
            "$group": {
                "_id": {
                    "Name": "$Name",
                    "Contact Details": "$Contact Details"
                },
                "Name": {"$first": "$Name"},
                "Contact Details": {"$first": "$Contact Details"},
                "Location": {"$first": "$Location"},
                "Job Skills": {"$first": "$Job Skills"},
                "Experience": {"$first": "$Experience"},
                "Projects": {"$first": "$Projects"},
                "Comments": {"$first": "$Comments"}
            }
        },
        {"$limit": 10}  
    ])
    return list(matching_profiles)


def retrieve_profiles_from_es(job_description):
    response = es.search(
        index='candidates',
        body={
            'query': {
                'match': {
                    'Job Skills': job_description
                }
            },
            'collapse': {
                'field': 'Contact Details.keyword'  
            },
            'size': 10  
        }
    )
    return [hit['_source'] for hit in response['hits']['hits']]

def generate_profiles(retrieved_profiles):
    formatted_profiles = []
    for profile in retrieved_profiles:
        profile_str = (
            f"Name: {profile['Name']}/n"
            f"Contact: {profile['Contact Details']}/n"
            f"Location: {profile['Location']}/n"
            f"Skills: {profile['Job Skills']}/n"
            f"Experience: {profile['Experience']}/n"
            f"Projects: {profile['Projects']}/n"
            f"Comments: {profile['Comments']}/n"
            "-------------------------"
        )
        formatted_profiles.append(profile_str)
    
    input_text = "Matching profiles:/n" + "/n".join(formatted_profiles)
    
   
    tokens = tokenizer.encode(input_text)
    if len(tokens) > 1024:
        input_text = tokenizer.decode(tokens[:1024])
    
    inputs = tokenizer(input_text, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def interactive_cli():
    print("Welcome to the Interactive Profile Matcher!")
    print("Type 'exit' to quit./n")

    while True:
        query = input("Enter job description: ")
        if query.lower() == 'exit':
            break

        source = input("Enter data source (mongo/es): ").lower()
        if source not in ['mongo', 'es']:
            print("Invalid source. Please enter 'mongo' or 'es'.")
            continue

        if source == 'mongo':
            profiles = retrieve_profiles_from_mongo(query)
        else:
            profiles = retrieve_profiles_from_es(query)

        if not profiles:
            print("No matching profiles found.")
        else:
            summary = generate_profiles(profiles)
            print("/nResults:/n")
            print(summary)
            print("/n")

if __name__ == "__main__":
    interactive_cli()
