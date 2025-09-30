# Example 06 from: PySpark RDD Tutorial | Learn with Examples

# Create empty RDD with partition
rdd2 = spark.sparkContext.parallelize([],10) #This creates 10 partitions
