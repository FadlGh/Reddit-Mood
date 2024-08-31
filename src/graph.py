import csv
import matplotlib.pyplot as plt
from collections import Counter

with open('data/comments.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    emotions = [row['Emotion'] for row in reader]

emotion_counts = Counter(emotions)

emotions = list(emotion_counts.keys())
counts = list(emotion_counts.values())
bar_colors = plt.cm.tab10.colors[:len(emotions)]

fig, ax = plt.subplots()
ax.bar(emotions, counts, color=bar_colors)

ax.set_ylabel('Count')
ax.set_title('Emotion Distribution')

plt.show()
