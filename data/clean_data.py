import json
import re

# Load your dataset
with open('essay_instructions_dataset.json', 'r') as file:
    data = json.load(file)


# Function to remove the specified section from the prompt
def clean_prompt(prompt):
    # Regular expression to match "Human: ... :"
    pattern = r'^Human: .*?: '
    return re.sub(pattern, '', prompt).strip()


# Process each item in the dataset
for item in data:
    item['prompt'] = clean_prompt(item['prompt'])

# Save the cleaned dataset
with open('cleaned_essay_instructions_dataset.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Cleaning completed and dataset saved as cleaned_essay_instructions_dataset.json")
