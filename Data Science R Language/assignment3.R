# Assignment 3

# Load dataset
url <- "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df <- read.csv(url)

# Create Average Score
df$Average_Score <- (
  df$sepal_length +
  df$sepal_width +
  df$petal_length +
  df$petal_width
) / 4

# Sort dataset in ascending order
sorted_data <- df[order(df$Average_Score), ]

# Display first 10 rows
print(head(sorted_data, 10))
