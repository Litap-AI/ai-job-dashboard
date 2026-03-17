import pandas as pd

# Load dataset
def load_data():
    return pd.read_csv("output/jobs.csv")


# Filter by location
def filter_by_location(df, location):
    return df[df["India Locations"].str.contains(location, case=False, na=False)]


# Filter by role
def filter_by_role(df, role):
    return df[df["Roles Open (typical)"].str.contains(role, case=False, na=False)]


# Combined filter
def filter_jobs(location=None, role=None):
    df = load_data()

    if location:
        df = filter_by_location(df, location)

    if role:
        df = filter_by_role(df, role)

    return df


# Run example
if __name__ == "__main__":
    results = filter_jobs(location="Pune", role="Data")
    print(results)
