# Example 06 from: PySpark – Create an Empty DataFrame & RDD

#Create empty DatFrame with no schema (no columns)
df3 = spark.createDataFrame([], StructType([]))
df3.printSchema()

#print below empty schema
#root
