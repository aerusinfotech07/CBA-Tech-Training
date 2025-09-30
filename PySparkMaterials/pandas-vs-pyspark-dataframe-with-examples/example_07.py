# Example 07 from: Pandas vs PySpark DataFrame With Examples

# Create PySpark DataFrame from Pandas
pysparkDF2 = spark.createDataFrame(pandasDF) 
pysparkDF2.printSchema()
pysparkDF2.show()
