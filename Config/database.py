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
        f"mongodb+srv://krssn:{password}@dyslexia.9bswy.mongodb.net/?retryWrites=true&w=majority&appName=Dyslexia",
        tls=True,  # Use TLS for encryption
        tlsAllowInvalidCertificates=True  # Optionally allow invalid certs
    )
    
    # Access the specified database
    db = client.dyscalculia
    print("connection done")
    # Define the collections you will be working with
    user_registration_collection = db["Users_Reg"]
    user_profile_collection = db["User_Profile"]
    quiz_collection = db["Quizzes"]
    #questions_collection = db["QuizQuestions"]
    predicted_values_collection = db["PredictedResults"]
except Exception as e:
    print(f"error connecting: {e}")
