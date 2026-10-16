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

# Shapiro-Wilk for top-level
w1, p1 = stats.shapiro(top)
print("Top-level (n=" + str(len(top)) + ")")
print("  W = " + str(round(w1, 4)))
print("  p = " + str(round(p1, 4)))
if p1 < 0.05:
    print("  Result: NOT normal")
else:
    print("  Result: normal")

print()

# Shapiro-Wilk for replies
w2, p2 = stats.shapiro(rep)
print("Replies (n=" + str(len(rep)) + ")")
print("  W = " + str(round(w2, 4)))
print("  p = " + str(round(p2, 4)))
if p2 < 0.05:
    print("  Result: NOT normal")
else:
    print("  Result: normal")
with open('../results/shapiro_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['group', 'n', 'W', 'p_value', 'normal'])
    writer.writerow(['top-level', len(top), round(w1, 4), round(p1, 4), 'no' if p1 < 0.05 else 'yes'])
    writer.writerow(['replies', len(rep), round(w2, 4), round(p2, 4), 'no' if p2 < 0.05 else 'yes'])

print("\nSaved to ../results/shapiro_results.csv")