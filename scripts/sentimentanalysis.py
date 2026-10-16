import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
rows = []
with open('../data/clean_reddit_comments.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)
print("Total comments: " + str(len(rows)))

for row in rows:
    body = row.get('body', '') or ''
    score = analyzer.polarity_scores(body)
    row['sentiment'] = score['compound']
    row['depth'] = int(row.get('depth', 0) or 0)
    row['score'] = int(row.get('score', 0) or 0)

total = sum(float(r['sentiment']) for r in rows)
mean = total / len(rows)
print("Mean sentiment: " + str(round(mean, 4)))

top = [float(r['sentiment']) for r in rows if r['depth'] == 0]
rep = [float(r['sentiment']) for r in rows if r['depth'] > 0]
top_mean = sum(top) / len(top)
rep_mean = sum(rep) / len(rep)
print("Top-level mean: " + str(round(top_mean, 4)) + " (n=" + str(len(top)) + ")")
print("Replies mean:   " + str(round(rep_mean, 4)) + " (n=" + str(len(rep)) + ")")


depths = {}
for r in rows:
    d = r['depth']
    depths.setdefault(d, []).append(float(r['sentiment']))
print("\nSentiment by depth:")
for d in sorted(depths.keys()):
    vals = depths[d]
    print("  depth " + str(d) + ": mean=" + str(round(sum(vals)/len(vals), 4)) + " (n=" + str(len(vals)) + ")")

def pearson(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = (sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)) ** 0.5
    return num / den if den else 0

xs = [float(r['sentiment']) for r in rows]
ys = [float(r['score']) for r in rows]
print("\nCorrelation (sentiment vs score): " + str(round(pearson(xs, ys), 4)))

sorted_rows = sorted(rows, key=lambda r: float(r['sentiment']))
print("\nMost NEGATIVE comment:")
print("  " + sorted_rows[0]['body'][:200])
print("Most POSITIVE comment:")
print("  " + sorted_rows[-1]['body'][:200])

with open('comments_with_sentiment.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'id', 'author', 'body', 'score', 'created_utc',
        'depth', 'parent_id', 'controversiality', 'sentiment'
    ])
    writer.writeheader()
    writer.writerows(rows)

print("\nSaved to comments_with_sentiment.csv")
