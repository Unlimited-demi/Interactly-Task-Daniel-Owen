from transformers import GPT2Tokenizer, GPT2LMHeadModel
from pymongo import MongoClient

tokenizer = GPT2Tokenizer.from_pretrained('C:/Users/USER/Documents/Projects/Profile_matching/models/fine_tuned_gpt2')
model = GPT2LMHeadModel.from_pretrained('C:/Users/USER/Documents/Projects/Profile_matching/models/fine_tuned_gpt2')
uri = "mongodb+srv://unlimiteddemi:Kmyh4MSII9tHbbIK@cluster0.ddje26o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(uri)

db = client['candidate_db']
profiles_collection = db['profiles']

def retrieve_profiles(job_description):
    matching_profiles = profiles_collection.find({"Job Skills": {"$regex": job_description, "$options": "i"}})
    return list(matching_profiles)

def generate_profiles(retrieved_profiles):
    input_text = "Matching profiles:/n" + "/n".join([str(profile) for profile in retrieved_profiles])
    inputs = tokenizer(input_text, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
