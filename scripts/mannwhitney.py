import csv
from scipy import stats
top = []
rep = []
with open('../data/comments_with_sentiment.csv', 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        s = float(row['sentiment'])
        d = int(row['depth'])
        if d == 0:
            top.append(s)
        else:
            rep.append(s)
u, p = stats.mannwhitneyu(top, rep, alternative='two-sided')
print("Top-level (n=" + str(len(top)) + ")")
print("Replies   (n=" + str(len(rep)) + ")")
print("U = " + str(u))
print("p = " + str(round(p, 6)))

if p < 0.05:
    print("Result: SIGNIFICANT")
else:
    print("Result: NOT significant")
with open('../results/mannwhitney_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['test', 'U', 'p_value'])
    writer.writerow(['mann_whitney', u, round(p, 6)])

print("\nSaved to ../results/mannwhitney_results.csv")
