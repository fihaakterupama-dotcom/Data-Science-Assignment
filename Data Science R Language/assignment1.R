# Assignment 1

# Load dataset from the internet
url <- "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df <- read.csv(url)

# Display first 5 rows
cat("First 5 Rows:\n")
head(df, 5)

# Display column names
cat("\nColumn Names:\n")
colnames(df)

# Display number of rows and columns
cat("\nNumber of Rows:", nrow(df), "\n")
cat("Number of Columns:", ncol(df), "\n")

# Display summary statistics
cat("\nSummary Statistics:\n")
summary(df)