# Example 06 from: PySpark 4.0 Tutorial For Beginners with Examples

# Create DataFrame from CSV file
df = spark.read.csv("/tmp/resources/zipcodes.csv")
df.printSchema()
