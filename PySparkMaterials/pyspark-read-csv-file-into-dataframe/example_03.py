# Example 03 from: PySpark Read CSV file into DataFrame

# Use header record for column names
df2 = spark.read.option("header",True) \
     .csv("/path/zipcodes.csv")
