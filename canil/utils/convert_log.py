import json
from datetime import datetime

def process_log_entry(log_entry):
    try:
        timestamp_str, info_str = log_entry.split("] ", 1)

        timestamp = datetime.strptime(timestamp_str[1:], "%Y-%m-%d %H:%M:%S")

        # Remove the "New Animal Registered - " prefix
        info_str = info_str.replace("New Animal Registered - ", "").replace("INFO: ", "").replace("WARNING: Health Check Required - ", "").replace("ALERT: Animal Missing - ", "")
        print(info_str)
        animal_info = {}
        for item in info_str.split(", "):
            print(item)
            key, value = item.split(": ", 1)
            animal_info[key] = value

        animal = {
            #'timestamp': timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'animal_type': animal_info.get('Animal_type')[0],
            'breed': animal_info.get('Breed'),
            'name': animal_info.get('Name'),
            'age': int(animal_info.get('Animal_age').replace(" years", "").replace(" year", "")),
            'size': animal_info.get('Size_of_animal')[0],
            'gender': animal_info.get('Sex_of_animal')[0],
            'owner': animal_info.get('Human_Owner'),
            'status': animal_info.get('Animal_condition')[0]
        }
        print(animal)

        return animal
    except Exception as e:
        print(f"Error processing log entry: {e}")
        return None

log_file_path = 'lecacy_animals.txt'
json_output_file = 'output.json'

with open(log_file_path, 'r') as file:
    log_entries = file.readlines()

animals = [process_log_entry(entry) for entry in log_entries if entry.strip()]

animals = list(filter(None, animals))

with open(json_output_file, 'w') as json_file:
    json.dump(animals, json_file, indent=2)

print(f"Data written to {json_output_file}")