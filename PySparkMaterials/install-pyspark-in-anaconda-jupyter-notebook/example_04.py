# Example 04 from: Install PySpark in Anaconda & Jupyter Notebook

# Import PySpark
from pyspark.sql import SparkSession

#Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# Data
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

# Columns
columns = ["language","users_count"]

# Create DataFrame
df = spark.createDataFrame(data).toDF(*columns)

# Print DataFrame
df.show()
