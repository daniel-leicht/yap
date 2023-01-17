def process_data(data, user_name, user_age, user_gender, user_location, user_email, user_phone):
    processed_data = {}
    if user_name != "":
        processed_data["name"] = user_name
    if user_age != "":
        processed_data["age"] = user_age
    if user_gender != "":
        processed_data["gender"] = user_gender
    if user_location != "":
        processed_data["location"] = user_location
    if user_email != "":
        processed_data["email"] = user_email
    if user_phone != "":
        processed_data["phone"] = user_phone

    for record in data:
        if "name" in processed_data:
            record["name"] = processed_data["name"]
        if "age" in processed_data:
            record["age"] = processed_data["age"]
        if "gender" in processed_data:
            record["gender"] = processed_data["gender"]
        if "location" in processed_data:
            record["location"] = processed_data["location"]
        if "email" in processed_data:
            record["email"] = processed_data["email"]
        if "phone" in processed_data:
            record["phone"] = processed_data["phone"]

    return data

data = [{"name": "John", "age": 25, "gender": "male", "location": "New York", "email": "john@example.com", "phone": "555-555-5555"},
        {"name": "Jane", "age": 30, "gender": "female", "location": "Los Angeles", "email": "jane@example.com", "phone": "444-444-4444"}]

user_name = "Jane"
user_age = ""
user_gender = ""
user_location = ""
user_email = "new_email@example.com"
user_phone = ""

print(process_data(data, user_name, user_age, user_gender, user_location, user_email, user_phone))