import json
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("iamketan25/essay-instructions-dataset")

# Extract the train split
train_split = dataset['train']

# Create a list of dictionaries with 'prompt' and 'chosen'
data = []
for item in train_split:
    data.append({
        "prompt": item['prompt'],
        "chosen": item['chosen']
    })

# Serialize the list of dictionaries to a JSON formatted string
dataset_json = json.dumps(data, indent=2)

# Save the JSON to a file
json_path = "essay_instructions_dataset.json"
with open(json_path, "w") as json_file:
    json_file.write(dataset_json)

print(f"Dataset saved to {json_path}")