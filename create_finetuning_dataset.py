import json


# Function to format the data
def format_training_data(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
        return

    training_data = []

    for entry in data:
        prompt = entry['prompt']
        expected_output = entry['chosen']

        training_entry = {
            "messages": [
                {
                    "role": "system",
                    "content": """You are an AI research paper assistant that writes full sections of research papers based on a single prompt. Your responses must sound human to bypass AI detectors. If the user provides specific data, use that in your response to enhance credibility and depth.
                    
                    Ensure your writing includes natural language patterns, varied sentence structures, and a coherent flow. Use idiomatic expressions, appropriate tone, and contextually relevant vocabulary. Integrate transitions between paragraphs and ideas smoothly. Pay attention to grammar, punctuation, and spelling. Incorporate critical thinking and logical reasoning to support arguments."""
                },
                {
                    "role": "user",
                    "content": f"Prompt: \"{prompt}\" \n\nData: no data provided by this user"
                },
                {
                    "role": "assistant",
                    "content": expected_output
                }
            ]
        }

        training_data.append(training_entry)

    # Save the formatted data to the output file
    with open(output_file, 'w') as f:
        json.dump(training_data, f, indent=4)

    print(
        f"Training data creation complete. The results have been saved to {output_file}")


# Run the function to create training data
format_training_data('./data/essay_instructions_dataset.json',
                     './data/training_dataset.json')
