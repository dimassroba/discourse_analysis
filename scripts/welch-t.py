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

t, p = stats.ttest_ind(top, rep, equal_var=False)
print("t = " + str(round(t, 4)))
print("p = " + str(round(p, 4)))
with open('../results/ttest_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['test', 'statistic', 'p_value', 'group1_mean', 'group1_n', 'group2_mean', 'group2_n'])
    writer.writerow(['welch_ttest', round(t, 4), round(p, 4),
                     round(sum(top)/len(top), 4), len(top),
                     round(sum(rep)/len(rep), 4), len(rep)])

print("\nSaved to ../results/ttest_results.csv")