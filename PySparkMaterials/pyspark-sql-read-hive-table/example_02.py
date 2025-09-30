# Example 02 from: PySpark SQL Read Hive Table

# Read Hive table
df = spark.sql("select * from emp.employee")
df.show()
