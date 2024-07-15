import json
import os
import random
from datasets import load_dataset

def prepare_figqa_train_data(output_dir, train_ratio=0.8, valid_ratio=0.1):
    # Load the FIG-QA dataset from Hugging Face
    figqa_train_dataset = load_dataset('nightingal3/fig-qa', split='train')
    
    # Mapping for labels
    label_map = {0: "Entails", 1: "Contradicts"}

    # Convert to the desired format for training data
    converted_train_data = []
    for i, example in enumerate(figqa_train_dataset):
        if int(example['labels']) in label_map:  # Include only Entailment and Contradiction
            en1 = f'Does the sentence "{example["ending1"]}" entail or contradict the sentence "{example["startphrase"]}"? Please answer between "Entailment" or "Contradiction" and explain your decision in a sentence.'
            en2 = f'{label_map[int(example["labels"])]}.'
            converted_example = {
                "translation": {
                    "en1": en1,
                    "en2": en2
                }
            }
            converted_train_data.append(converted_example)

    # Shuffle data
    random.shuffle(converted_train_data)

    # Split the data into train, validation, and test sets
    total_train_samples = len(converted_train_data)
    train_end = int(train_ratio * total_train_samples)
    valid_end = train_end + int(valid_ratio * total_train_samples)
    
    train_data = converted_train_data[:train_end]
    valid_data = converted_train_data[train_end:valid_end]
    test_data = converted_train_data[valid_end:]

    # Save to JSON files
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'figqa_train.json'), 'w') as f:
        for entry in train_data:
            f.write(json.dumps(entry) + '\n')
    
    with open(os.path.join(output_dir, 'figqa_valid.json'), 'w') as f:
        for entry in valid_data:
            f.write(json.dumps(entry) + '\n')

    with open(os.path.join(output_dir, 'figqa_test.json'), 'w') as f:
        for entry in test_data:
            f.write(json.dumps(entry) + '\n')

    print(f"Train, validation, and test datasets saved to {output_dir}")

if __name__ == "__main__":
    output_directory = '/content/model-in-the-loop-fig-lang/'
    prepare_figqa_train_data(output_directory)
