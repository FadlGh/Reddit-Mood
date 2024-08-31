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

subreddit = reddit.subreddit("technews")
subreddit_top = subreddit.top(limit=1)

with open('data/comments.csv', 'w', newline='', encoding='utf-8') as c:
    fieldnames = ['Text', 'Emotion']
    writer = csv.DictWriter(c, fieldnames=fieldnames)
    writer.writeheader()

    for post in subreddit_top:
        post.comments.replace_more(limit=0)

        for comment in post.comments.list()[:5]:
            writer.writerow({'Text': comment.body, 'Emotion': 'neutral'})
