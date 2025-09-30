# Example 05 from: PySpark Read and Write MySQL Database Table

# Using numPartitions
df = spark.read \
  .format("jdbc") \
  .option("query", "select id,age from employee where gender='M'") \
  .option("numPartitions",4) \
  .option("fetchsize", 20) \
  .......
  .......
  .load()
