import csv
from scipy import stats
sentiment = []
upvotes = []

with open('../data/comments_with_sentiment.csv', 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        s = float(row['sentiment'])
        v = int(row['score'])
        sentiment.append(s)
        upvotes.append(v)
r, p = stats.pearsonr(sentiment, upvotes)
print("Pearson correlation")
print("  r = " + str(round(r, 4)))
print("  p = " + str(round(p, 4)))
rho, p2 = stats.spearmanr(sentiment, upvotes)
print()
print("Spearman rank correlation")
print("  rho = " + str(round(rho, 4)))
print("  p = " + str(round(p2, 4)))

with open('../results/correlation_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['test', 'statistic', 'p_value'])
    writer.writerow(['pearson', round(r, 4), round(p, 4)])
    writer.writerow(['spearman', round(rho, 4), round(p2, 4)])

print("\nSaved to ../results/correlation_results.csv")
print()
if p < 0.05:
    if r > 0:
        print("Significant POSITIVE: positive comments get more upvotes")
    else:
        print("Significant NEGATIVE: negative comments get more upvotes")
else:
    print("NOT significant: upvotes don't track sentiment")
