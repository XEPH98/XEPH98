import json

with open("end_plate/data/proj1.json") as f:
    data = json.load(f)

# Example of accessing values
print(data["end_plate"]["width"])  # 250.0
