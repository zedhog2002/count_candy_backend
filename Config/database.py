from pymongo import MongoClient
from urllib.parse import quote_plus

username = quote_plus("krssn")
password = quote_plus("krssn@capstone")

client = MongoClient(
    f"mongodb+srv://{username}:{password}@dyslexia.9bswy.mongodb.net/?retryWrites=true&w=majority&appName=Dyslexia",
    tls=True,  # Use tls instead of ssl
    tlsAllowInvalidCertificates=True  # Ignore invalid certificates
)

db = client.dyscalculia

# Change the collection names as needed
user_registration_collection = db["UserRegistrations"]
user_profile_collection = db["UserProfiles"]
quiz_collection = db["Quizzes"]
questions_collection = db["QuizQuestions"]
predicted_values_collection = db["PredictedResults"]

# Now, your collections have the updated names


