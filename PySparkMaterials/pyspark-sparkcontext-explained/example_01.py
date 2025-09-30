# Example 01 from: PySpark SparkContext Explained

# Create SparkSession from builder
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]") \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()
print(spark.sparkContext)
print("Spark App Name : "+ spark.sparkContext.appName)

# Outputs
#<SparkContext master=local[1] appName=SparkByExamples.com>
#Spark App Name : SparkByExamples.com
