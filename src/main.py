import pandas as pd
from analyzer import find_groups
from explainer import explain_group
from recommender import recommend

df = pd.read_csv("data/sample_students.csv")
df = find_groups(df)

for g in df["group"].unique():
    print("\n=== Group:", g, "===")
    print("Explanation:", explain_group(df, g))
    print("Recommendations:")
    for r in recommend(df, g):
        print("-", r)
