import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df = pd.read_csv(url)

# Create Average Score
df["Average Score"] = (
    df["sepal_length"] +
    df["sepal_width"] +
    df["petal_length"] +
    df["petal_width"]
) / 4

# Sort data by Average Score (Ascending)
sorted_df = df.sort_values(by="Average Score", ascending=True)

print(sorted_df.head())
print(sorted_df.head())