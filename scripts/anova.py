import csv
from scipy import stats
depths = {}
with open('../data/comments_with_sentiment.csv', 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        d = int(row['depth'])
        s = float(row['sentiment'])
        depths.setdefault(d, []).append(s)
print("Group sizes:")
for d in sorted(depths.keys()):
    print("  depth " + str(d) + ": n=" + str(len(depths[d])))
groups = [depths[d] for d in sorted(depths.keys()) if len(depths[d]) >= 2]
f_stat, p = stats.f_oneway(*groups)
print()
print("One-way ANOVA")
print("  F = " + str(round(f_stat, 4)))
print("  p = " + str(round(p, 4)))
if p < 0.05:
    print("  Result: SIGNIFICANT — sentiment differs across depths")
else:
    print("  Result: NOT significant — depth does not explain sentiment")
# Kruskalwallis
h_stat, p2 = stats.kruskal(*groups)
print()
print("Kruskal-Wallis (non-parametric)")
print("  H = " + str(round(h_stat, 4)))
print("  p = " + str(round(p2, 4)))
if p2 < 0.05:
    print("  Result: SIGNIFICANT")
else:
    print("  Result: NOT significant")
with open('../results/anova_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['test', 'statistic', 'p_value'])
    writer.writerow(['anova', round(f_stat, 4), round(p, 4)])
    writer.writerow(['kruskal_wallis', round(h_stat, 4), round(p2, 4)])

print("\nSaved to ../results/anova_results.csv")
