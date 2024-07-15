import json
import os
import random
from datasets import load_dataset

def prepare_mnli_data(output_dir, train_ratio=0.8, valid_ratio=0.1):
    # Load the MNLI dataset from GLUE
    mnli_dataset = load_dataset('glue', 'mnli', split='validation_matched')
    
    # Mapping for labels
    label_map = {0: "Entails", 2: "Contradicts"}

    # Convert to the desired format
    converted_data = []
    for i, example in enumerate(mnli_dataset):
        if example['label'] in label_map:  # Include only Entailment and Contradiction
            en1 = f'Does the sentence "{example["premise"]}" entail or contradict the sentence "{example["hypothesis"]}"? Please answer between "Entails" or "Contradicts" and explain your decision in a sentence.'
            en2 = f'{label_map[example["label"]]}. '
            converted_example = {
                "translation": {
                    "en1": en1,
                    "en2": en2
                }
            }
            converted_data.append(converted_example)

    # Shuffle data
    random.shuffle(converted_data)

    # Split the data into train, validation, and test sets
    total_samples = len(converted_data)
    train_end = int(train_ratio * total_samples)
    valid_end = train_end + int(valid_ratio * total_samples)
    
    train_data = converted_data[:train_end]
    valid_data = converted_data[train_end:valid_end]
    test_data = converted_data[valid_end:]

    # Save to JSON files
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'mnli_train.json'), 'w') as f:
        for entry in train_data:
            f.write(json.dumps(entry) + '\n')
    
    with open(os.path.join(output_dir, 'mnli_valid.json'), 'w') as f:
        for entry in valid_data:
            f.write(json.dumps(entry) + '\n')

    with open(os.path.join(output_dir, 'mnli_test.json'), 'w') as f:
        for entry in test_data:
            f.write(json.dumps(entry) + '\n')

    print(f"Train, validation, and test datasets saved to {output_dir}")

if __name__ == "__main__":
    output_directory = '/content/model-in-the-loop-fig-lang/'
    prepare_mnli_data(output_directory)
