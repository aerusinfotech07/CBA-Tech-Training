# Example 04 from: PySpark Read CSV file into DataFrame

# Read multiple CSV files
df = spark.read.csv("path/file1.csv,path/file2.csv,path/file3.csv")
