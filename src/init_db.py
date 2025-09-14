from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['school']
activities_collection = db['activities']

# Initial activities data
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in local matches",
        "schedule": "Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 18,
        "participants": []
    },
    "Swimming Club": {
        "description": "Practice swimming techniques and participate in meets",
        "schedule": "Thursdays, 5:00 PM - 6:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Art Workshop": {
        "description": "Explore painting, drawing, and sculpture with peers",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Drama Club": {
        "description": "Act, direct, and produce plays for the school community",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": []
    },
    "Math Olympiad": {
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 10,
        "participants": []
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": []
    }
}

# Drop existing activities collection to start fresh
activities_collection.drop()

# Insert activities with their names as keys
for name, details in activities.items():
    activity_doc = details.copy()
    activity_doc['name'] = name  # Add name field to the document
    activities_collection.insert_one(activity_doc)

print("Database initialized with activities!")

# Verify the data
print("\nActivities in database:")
for activity in activities_collection.find():
    print(f"- {activity['name']}: {activity['participants']} participants")