# Load dataset
url <- "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df <- read.csv(url)

# Create Average Score column
df$Average_Score <- (
    df$sepal_length + df$sepal_width +
    df$petal_length + df$petal_width
) / 4

# Apply condition
df$Category <- ifelse(df$Average_Score >= 3.5, "High", "Low")

# Display first 5 rows
print(head(df))
