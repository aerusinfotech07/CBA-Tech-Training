# Example 04 from: PySpark 4.0 Tutorial For Beginners with Examples

# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate() 

# Create RDD from external Data source
rdd2 = spark.sparkContext.textFile("/path/test.txt")
