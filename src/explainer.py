def explain_group(df, group_id):
    group = df[df["group"] == group_id]
    avg_score = group["score"].mean()
    avg_attention = group["attention_span"].mean()
    avg_watch = group["watch_time"].mean()

    if avg_score < 60:
        return "This group has low scores and may lack foundational understanding."

    if avg_attention < 0.5:
        return "This group struggles with attention span. Shorter, engaging material may help."

    if avg_watch < 90:
        return "This group is not watching enough content. They may need interactive lessons."

    return "This group is performing within a normal range."
