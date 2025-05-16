from pymongo import MongoClient

# Connect to MongoDB (change URI as needed)
client = MongoClient("mongodb+srv://dhruvsandhu21:dhruvsandhu21@cluster0.n2ipt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Select your database and collection
db = client['mydatabase']
collection = db['mycollection']

# Get and print database and collection names
print("Database Name:", collection.database.name)
print("Collection Name:", collection.name)