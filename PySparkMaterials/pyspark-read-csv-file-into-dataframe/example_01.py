# Example 01 from: PySpark Read CSV file into DataFrame

# Import
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder().master("local[1]")
          .appName("SparkByExamples.com")
          .getOrCreate()

# Read CSV File
df = spark.read.csv("/path/zipcodes.csv")
df.printSchema()
