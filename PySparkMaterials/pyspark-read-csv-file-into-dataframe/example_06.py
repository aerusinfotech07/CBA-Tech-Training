# Example 06 from: PySpark Read CSV file into DataFrame

# Using delimiter option
df3 = spark.read.options(delimiter=',') \
  .csv("/path/zipcodes.csv")
