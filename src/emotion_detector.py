from transformers import pipeline

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

text = "I am gonna fucking die from this bullshit."
result = classifier(text)

print(result)