# Example 01 from: PySpark Create DataFrame with Examples

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
rdd = spark.sparkContext.parallelize(data)
