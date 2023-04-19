import pymongo
import os

client = pymongo.MongoClient(
    os.getenv("MONGODB_URI"),  # "mongodb://localhost:27017"
    tls=True,
    tlsAllowInvalidCertificates=True
)

db = client["test"]

Movies = db["movies"]

Movies.insert_one({
    "title": "Monty Python and the Holy Grail",
    "year": 1975,
    "score": 8.2
})

result = Movies.find_one({"title": "Monty Python and the Holy Grail"})
print(result["_id"])

result2 = Movies.find_one({"_id": result["_id"]})
print(result2)
