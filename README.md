**Sentiment and depth in a Reddit Thread: A small scale analysis**

---

Overview

This project analyzes the emotional structure of a controversial Reddit thread. Using VADER sentiment analysis on 178 comments from an r/AskReddit thread, three hypotheses are tested:

1. Do top-level comments differ in sentiment from replies?
2. Does sentiment change with thread depth?
3. Do upvotes track sentiment?

---

Key Findings

Finding:                                                                    Result:
Top-level comments are more negative than replies                           Welch's t = -2.69, p = 0.010;     Mann-Whitney U = 1509.5, p = 0.006
Sentiment warms with thread depth                                           ANOVA F = 2.43, p = 0.037;        Kruskal-Wallis H = 12.05, p = 0.034
Upvotes do not track sentiment                                              Pearson r = -0.057, p = 0.449;    Spearman rho = -0.056, p = 0.461

Interpretation: 
1. Controversial threads exhibit a provocation–response structure. 
2. Hostility concentrates at the top. Deeper comments trend warmer. 
3. And Reddit's voting mechanism rewards agreement or provocation, not emotional tone.

---
