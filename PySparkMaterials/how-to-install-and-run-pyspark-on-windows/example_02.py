# Example 02 from: How to Install PySpark on Windows

# RDD creation
rdd = spark.sparkContext.parallelize([1,2,3,4,5,6])
print(rdd.count)
