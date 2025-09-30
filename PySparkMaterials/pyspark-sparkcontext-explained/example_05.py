# Example 05 from: PySpark SparkContext Explained

# Create RDD
rdd = spark.sparkContext.range(1, 5)
print(rdd.collect())

# Output
#[1, 2, 3, 4]
