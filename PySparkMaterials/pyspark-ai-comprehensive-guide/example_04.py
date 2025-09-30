# Example 04 from: PySpark AI (pyspark-ai) – English SDK Comprehensive Guide

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.getOrCreate()

# Create SparkAI by using existing SparkSession object
spark_ai = SparkAI(spark_session=spark, verbose=True)
