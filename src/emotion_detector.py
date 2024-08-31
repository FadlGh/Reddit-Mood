from transformers import pipeline
import csv

# Initialize the emotion classifier
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Read the CSV file
with open('data/comments.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Update the Emotion column
for row in rows:
    # Apply the classifier to the text and extract the emotion label
    classification = classifier(row['Text'])
    row['Emotion'] = classification[0]['label']  # Extract the emotion label
    print(row['Emotion'])

# Write the updated data back to the CSV file
with open('data/comments.csv', 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['Text', 'Emotion']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
