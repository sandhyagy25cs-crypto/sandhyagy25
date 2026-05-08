def recommend(df, group_id):
    group = df[df["group"] == group_id]
    recs = []

    if group["score"].mean() < 60:
        recs.append("Provide simpler lessons and extra practice quizzes.")

    if group["watch_time"].mean() < 90:
        recs.append("Use interactive videos to boost engagement.")

    if group["attention_span"].mean() < 0.5:
        recs.append("Break lessons into shorter chunks.")

    if len(recs) == 0:
        recs.append("This group is performing well. Maintain regular support.")

    return recs
