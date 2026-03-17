def filter_jobs(df, location, role):
    filtered = df.copy()

    # --- Filter by Location ---
    if location != "All":
        filtered = filtered[
            filtered["India Locations"].str.contains(location, case=False, na=False)
        ]

    # --- Filter by Role ---
    if role != "All":
        filtered = filtered[
            filtered["Roles Open (typical)"].str.contains(role, case=False, na=False)
        ]

    return filtered
