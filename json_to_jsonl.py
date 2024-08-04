import json


def json_to_jsonl(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {input_file}.")
        return

    with open(output_file, 'w') as f:
        for entry in data:
            f.write(json.dumps(entry) + '\n')

    print(
        f"Conversion complete. The JSONL file has been saved to {output_file}")


# Run the function to convert JSON to JSONL
json_to_jsonl('./data/training_dataset.json',
              './data/training_dataset.jsonl')
