# Example 01 from: PySpark RDD Tutorial | Learn with Examples

# Imports
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder
      .master("local[1]")
      .appName("SparkByExamples.com")
      .getOrCreate()
