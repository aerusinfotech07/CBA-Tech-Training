# Example 05 from: PySpark Query Database Table using JDBC

# Using numPartitions
df = spark.read \
  .format("jdbc") \
  .option("query", "select id,age from employee where gender='M'") \
  .option("numPartitions",5) \
  .option("fetchsize", 20) \
  .......
  .......
  .load()
