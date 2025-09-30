# Example 06 from: PySpark apply Function to Column

# Custom UDF with withColumn()
df.withColumn("Cureated Name", upperCaseUDF(col("Name"))) \
  .show(truncate=False)

# Custom UDF with select()  
df.select(col("Seqno"), \
    upperCaseUDF(col("Name")).alias("Name") ) \
   .show(truncate=False)

# Custom UDF with sql()
spark.udf.register("upperCaseUDF", upperCaseUDF)
df.createOrReplaceTempView("TAB")
spark.sql("select Seqno, Name, upperCaseUDF(Name) from TAB") \
     .show()
