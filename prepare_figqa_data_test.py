import json
import os
from datasets import load_dataset

def prepare_figqa_test_data(output_dir):
    # Load the FIG-QA dataset from Hugging Face
    figqa_valid_dataset = load_dataset('nightingal3/fig-qa', split='validation')
    
    # Mapping for labels
    label_map = {0: "Entailment", 1: "Contradiction"}

    # Convert to the desired format for validation data
    converted_valid_data = []
    for i, example in enumerate(figqa_valid_dataset):
        if int(example['labels']) in label_map:  # Include only Entailment and Contradiction
            converted_example = {
                "id": str(i),
                "premise": example["ending1"],
                "hypothesis": example["startphrase"],
                "label": label_map[int(example["labels"])],
                "explanation": ""
            }
            converted_valid_data.append(converted_example)

    # Save to JSON file
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'figqa_test.jsonl'), 'w') as f:
        for entry in converted_valid_data:
            f.write(json.dumps(entry) + '\n')

    print(f"Validation dataset saved to {output_dir}")

if __name__ == "__main__":
    output_directory = '/content/model-in-the-loop-fig-lang/testgolddata/'
    prepare_figqa_test_data(output_directory)
