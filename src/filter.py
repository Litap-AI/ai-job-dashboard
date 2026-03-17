import pandas as pd

def filter_jobs(df, location, role):
    filtered_df = df.copy()

    # --- Filter by Location ---
    if location != "All":
        filtered_df = filtered_df[
            filtered_df["India Locations"].str.contains(location, case=False, na=False)
        ]

    # --- Filter by Role ---
    if role != "All":
        filtered_df = filtered_df[
            filtered_df["Roles Open (typical)"].str.contains(role, case=False, na=False)
        ]

    return filtered_df
