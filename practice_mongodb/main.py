import os
from dotenv import load_dotenv
from pymongo import MongoClient
import rich

load_dotenv()


client = MongoClient(os.getenv("Db_url"))

db = client["myschooldb"] # we created databases

collection = db["students"] # we created collections/table

# studentData = {
#     "name": "sami",
#     "age": 10,
#     "gender": "male",
#     "class": 5,
#     "section": "A"}


# collection.insert_one(studentData)

data = collection.find({})

# # UPDATE
# collection.update_one(
#     {"name": "Samreen"},             # Filter
#     {"$set": {"age": 44, "gender": "female", "class": 18}}  # Update
# )
# rich.print("[red]Document inserted successfully.[/red]")

# DELETED
collection.delete_one({"name": "sami"})
rich.print("[blue]Document deleted successfully.[/blue]")
for i in data:
    rich.print(i)