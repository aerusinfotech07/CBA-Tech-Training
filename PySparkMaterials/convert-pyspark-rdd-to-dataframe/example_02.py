# Example 02 from: Convert PySpark RDD to DataFrame

deptDF = spark.createDataFrame(rdd, schema = deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)
