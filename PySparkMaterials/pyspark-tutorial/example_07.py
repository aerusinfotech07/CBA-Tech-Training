# Example 07 from: PySpark 4.0 Tutorial For Beginners with Examples

# Create temporary table
df.createOrReplaceTempView("PERSON_DATA")

# Run SQL query
df2 = spark.sql("SELECT * from PERSON_DATA")
df2.printSchema()
df2.show()
