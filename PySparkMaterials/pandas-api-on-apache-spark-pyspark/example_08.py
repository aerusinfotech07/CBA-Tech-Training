# Example 08 from: Pandas API on Spark | Explained With Examples

# Pandas API on Spark
pdf = ps.read_csv('/tmp/resources/courses.csv')

# PySpark
sdf = spark.read.csv("/tmp/resources/courses.csv")
