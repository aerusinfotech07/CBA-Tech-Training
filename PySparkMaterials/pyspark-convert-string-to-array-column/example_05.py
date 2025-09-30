# Example 05 from: PySpark Convert String to Array Column

# Run SQL query
df.createOrReplaceTempView("PERSON")
spark.sql("select SPLIT(name,',') as NameArray from PERSON") \
    .show()
