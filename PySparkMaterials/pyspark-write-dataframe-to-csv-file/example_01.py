# Example 01 from: PySpark Write to CSV File

# Import
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.master("local[1]") \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()

# Read CSV file into DataFrame
df = spark.read.csv("/tmp/resources/zipcodes.csv")
