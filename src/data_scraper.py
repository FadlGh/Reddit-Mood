import praw
import os
import csv
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret= os.getenv('CLIENT_KEY'),
    user_agent='Mood by u/Horror_Job_566',
    username='Horror_Job_566',
    password=os.getenv('PASSWORD')
)

subreddit = reddit.subreddit("Futurology")
subreddit_top = subreddit.top(limit=10000)

with open('data/comments.csv', 'a', newline='', encoding='utf-8') as c:
    fieldnames = ['Text', 'Emotion']
    writer = csv.DictWriter(c, fieldnames=fieldnames)

    c.seek(0, 2)
    if c.tell() == 0:
        writer.writeheader()

    for post in subreddit_top:
        post.comments.replace_more(limit=0)

        for comment in post.comments.list()[:3]:
            if len(comment.body) < 100 or len(comment.body) > 300 or 'http' in comment.body or 'www' in comment.body:
                continue
            writer.writerow({'Text': comment.body.strip(), 'Emotion': 'neutral'}) # use 'neutral' as a placeholder
