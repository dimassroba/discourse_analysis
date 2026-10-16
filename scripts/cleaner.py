import json
import csv

with open('../data/datavader.txt', 'r', encoding='utf-8') as f:
    data = json.load(f)

comments = []

def extract(children):
    for child in children:
        if child.get('kind') == 't1':
            d = child.get('data', {})
            body = d.get('body', '')
            if body and body not in ('[removed]', '[deleted]'):
                comments.append({
                    'id': d.get('id'),
                    'author': d.get('author'),
                    'body': body,
                    'score': d.get('score'),
                    'created_utc': d.get('created_utc'),
                    'depth': d.get('depth'),
                    'parent_id': d.get('parent_id'),
                    'controversiality': d.get('controversiality'),
                })
            replies = d.get('replies')
            if isinstance(replies, dict):
                sub = replies.get('data', {}).get('children', [])
                if sub:
                    extract(sub)

if len(data) > 1:
    extract(data[1].get('data', {}).get('children', []))

with open('clean_reddit_comments.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'id', 'author', 'body', 'score',
        'created_utc', 'depth', 'parent_id', 'controversiality'
    ])
    writer.writeheader()
    writer.writerows(comments)

print("Extracted " + str(len(comments)) + " comments.")