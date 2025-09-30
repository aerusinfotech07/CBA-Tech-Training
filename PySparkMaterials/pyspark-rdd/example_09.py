# Example 09 from: PySpark RDD Tutorial | Learn with Examples

# Converts RDD to DataFrame
dfFromRDD1 = rdd.toDF()

# Converts RDD to DataFrame with column names
dfFromRDD2 = rdd.toDF("col1","col2")

# using createDataFrame() - Convert DataFrame to RDD
df = spark.createDataFrame(rdd).toDF("col1","col2")

# Convert DataFrame to RDD
rdd = df.rdd
