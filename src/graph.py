import csv
import matplotlib.pyplot as plt
from collections import Counter

# Read the CSV file and extract emotions
with open('data/comments.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    emotions = [row['Emotion'] for row in reader]

# Count the occurrences of each emotion
emotion_counts = Counter(emotions)

# Remove the 'neutral' emotion from the counts
if 'neutral' in emotion_counts:
    del emotion_counts['neutral']

# Prepare data for plotting
emotions = list(emotion_counts.keys())
counts = list(emotion_counts.values())
bar_colors = plt.cm.tab10.colors[:len(emotions)]  # Generate distinct colors

# Create the bar chart
fig, ax = plt.subplots()
ax.bar(emotions, counts, color=bar_colors)

# Set labels and title
ax.set_ylabel('Count')
ax.set_title('Emotion Distribution')

# Show the plot
plt.show()
