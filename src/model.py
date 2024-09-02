from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import csv

with open('data/comments.csv', 'r', newline='', encoding='utf-8') as c:
    reader = csv.DictReader(c)
    rows = list(reader)

comments = [row['Text'] for row in rows[1:]]
labels = [row['Emotion'] for row in rows[1:]]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(comments)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.05, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)


