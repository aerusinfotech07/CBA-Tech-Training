# Example 04 from: PySpark – Create an Empty DataFrame & RDD

#Create empty DataFrame from empty RDD
df = spark.createDataFrame(emptyRDD,schema)
df.printSchema()
