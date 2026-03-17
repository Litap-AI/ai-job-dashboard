def calculate_score(row, location, role):
    score = 0

    # --- Location match ---
    if location != "All" and location.lower() in row["India Locations"].lower():
        score += 1

    # --- Role match ---
    if role != "All" and role.lower() in row["Roles Open (typical)"].lower():
        score += 1

    return score


def rank_jobs(df, location, role):
    ranked_df = df.copy()

    ranked_df["score"] = ranked_df.apply(
        lambda row: calculate_score(row, location, role),
        axis=1
    )

    ranked_df = ranked_df.sort_values(by="score", ascending=False)

    return ranked_df
