# Example 07 from: PySpark Read CSV file into DataFrame

# Using inferschema and delimiter
df4 = spark.read.options(inferSchema='True',delimiter=',') \
  .csv("/path/zipcodes.csv")
