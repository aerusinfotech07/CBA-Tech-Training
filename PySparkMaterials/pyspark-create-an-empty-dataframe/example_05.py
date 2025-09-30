# Example 05 from: PySpark – Create an Empty DataFrame & RDD

#Create empty DataFrame directly.
df2 = spark.createDataFrame([], schema)
df2.printSchema()
