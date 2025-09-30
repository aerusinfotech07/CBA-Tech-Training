# Example 09 from: PySpark Read CSV file into DataFrame

# Chaining multiple options
df4 = spark.read.option("inferSchema",True) \
                .option("delimiter",",") \
  .csv("/path/zipcodes.csv")
