import praw
import auth
import csv

reddit = praw.Reddit(
    client_id=auth.CLIENT_ID,
    client_secret=auth.CLIENT_KEY,
    user_agent='Mood by u/Horror_Job_566',
    username='Horror_Job_566',
    password=auth.PASSWORD
)

subreddit = reddit.subreddit("politics")
subreddit_top = subreddit.top(limit=100)

with open('data/comments.csv', 'w', newline='', encoding='utf-8') as c:
    fieldnames = ['Text', 'Emotion']
    writer = csv.DictWriter(c, fieldnames=fieldnames)
    writer.writeheader()

    for post in subreddit_top:
        post.comments.replace_more(limit=0)

        for comment in post.comments.list()[:3]:
            if len(comment.body) < 50 or len(comment.body) > 400 or 'http' in comment.body:
                continue
            print(len(comment.body))
            writer.writerow({'Text': comment.body, 'Emotion': 'neutral'})
