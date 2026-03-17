import pandas as pd


# --- Clean location string into list ---
def process_locations(loc_string):
    if pd.isna(loc_string):
        return []

    parts = loc_string.split(",")

    clean_locs = []
    for p in parts:
        clean = p.strip().split("(")[0].strip().lower()
        clean_locs.append(clean)

    return clean_locs


# --- Main Filter Function ---
def filter_jobs(df, location, role):
    filtered_df = df.copy()

    # --- Filter by Location ---
    if location != "All":
        filtered_df = filtered_df[
            filtered_df["India Locations"].apply(
                lambda x: location.lower() in process_locations(x)
            )
        ]

    # --- Filter by Role ---
    if role != "All":
        filtered_df = filtered_df[
            filtered_df["Roles Open (typical)"].str.contains(role, case=False, na=False)
        ]

    return filtered_df
