import json
file1_path = "C:/Users/larse/Desktop/intershop/AiTuningJSONS/WorkBundel.jsonl"
file2_path = "C:/Users/larse/Desktop/intershop/AiTuningJSONS/validierungsbundel.jsonl"

# Load the training set
with open(file1_path, 'r', encoding='utf-8') as f:
    training_dataset = [json.loads(line) for line in f]

# Training dataset stats
print("Number of examples in training set:", len(training_dataset))
if training_dataset and "messages" in training_dataset[0]:
    print("First example in training set:")
    for message in training_dataset[0]["messages"]:
        print(message)
else:
    print("Training dataset is empty or does not contain 'messages' key.")


# Load the validation set
with open(file2_path, 'r', encoding='utf-8') as f:
    validation_dataset = [json.loads(line) for line in f]

# Validation dataset stats
print("\nNumber of examples in validation set:", len(validation_dataset))
print("First example in validation set:")
for message in validation_dataset[0]["messages"]:
    print(message)