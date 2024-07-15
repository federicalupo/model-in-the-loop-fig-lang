import json
import os
from datasets import load_dataset

def prepare_mnli_data(output_path, num_samples=2000):
    # Load the MNLI dataset from GLUE
    mnli_dataset = load_dataset('glue', 'mnli', split='validation_matched')
    
    # Mapping for labels
    label_map = {0: "Entailment", 2: "Contradiction"}

    # Convert to the desired format and select only the first num_samples rows
    converted_data = []
    for i, example in enumerate(mnli_dataset):
        if len(converted_data) >= num_samples:
            break
        if example['label'] in label_map:  # Include only Entailment and Contradiction
            converted_example = {
                "id": str(i),
                "hypothesis": example['hypothesis'],
                "premise": example['premise'],
                "label": label_map[example['label']],
                "explanation": ""
            }
            converted_data.append(converted_example)

    # Save to JSON file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        for entry in converted_data:
            f.write(json.dumps(entry) + '\n')

    print(f"Converted dataset saved to {output_path}")

if __name__ == "__main__":
    output_file_path = '/content/model-in-the-loop-fig-lang/testgolddata/mnli_test.jsonl'
    prepare_mnli_data(output_file_path, num_samples=2000)
