# Example 10 from: PySpark Read CSV file into DataFrame

# Using header option
df3 = spark.read.options(header='True', inferSchema='True', delimiter=',') \
  .csv("/path/zipcodes.csv")
