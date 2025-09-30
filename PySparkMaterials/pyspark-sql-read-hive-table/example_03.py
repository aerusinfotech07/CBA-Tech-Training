# Example 03 from: PySpark SQL Read Hive Table

# Read Hive table
df = spark.read.table("employee")
df.show()
