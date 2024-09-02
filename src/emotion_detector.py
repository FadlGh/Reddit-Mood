from transformers import pipeline
import csv

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

with open('data/comments.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

for row in rows:
    classification = classifier(row['Text'])
    classification[0] = sorted(classification[0], key=lambda d: d['score'], reverse=True)
    
    if classification[0][0]['label'] == 'neutral':
        emotion_label = classification[0][1]['label']
    else:
        emotion_label = classification[0][0]['label']
    
    row['Emotion'] = emotion_label
    print(f"Classified Emotion: {emotion_label} for Text: {row['Text']}")

with open('data/comments.csv', 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['Text', 'Emotion']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
