from transformers import pipeline
import csv

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

with open('data/comments.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

for row in rows:
    classification = classifier(row['Text'])
    emotion_label = classification[0]['label']
    row['Emotion'] = emotion_label
    print(f"Classified Emotion: {emotion_label} for Text: {row['Text']}")

filtered_rows = [row for row in rows if row['Emotion'].lower() != 'neutral']

with open('data/comments.csv', 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['Text', 'Emotion']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_rows)
