import pandas as pd
from sklearn.cluster import KMeans

def find_groups(df):
    features = df[["score", "watch_time", "assignments_completed", "attention_span"]]
    kmeans = KMeans(n_clusters=3, random_state=0)
    df["group"] = kmeans.fit_predict(features)
    return df
