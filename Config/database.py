import os
from pymongo import MongoClient
from urllib.parse import quote_plus

# Read the MongoDB credentials from environment variables
username = quote_plus(os.getenv("MONGO_USERNAME"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))
db_name = os.getenv("MONGO_DB_NAME")
mongo_url = os.getenv("MONGO_URL")

# Create the MongoDB client using environment variables
try:
    client = MongoClient(
        f"mongodb+srv://{username}:{password}@{mongo_url}/?retryWrites=true&w=majority&appName={db_name}",
        tls=True,  # Use TLS for encryption
        tlsAllowInvalidCertificates=True  # Optionally allow invalid certs
    )
    
    # Access the specified database
    db = client.dyscalculia
    print("connection done")
    # Define the collections you will be working with
    user_registration_collection = db["UserRegistrations"]
    user_profile_collection = db["UserProfiles"]
    quiz_collection = db["Quizzes"]
    questions_collection = db["QuizQuestions"]
    predicted_values_collection = db["PredictedResults"]
except Exception as e:
    print(f"error connecting: {e}")
