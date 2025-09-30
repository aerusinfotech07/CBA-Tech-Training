# Example 04 from: PySpark RDD Tutorial | Learn with Examples

# Read entire file into a RDD as single record.
rdd3 = spark.sparkContext.wholeTextFiles("/path/textFile.txt")
