# Example 09 from: What is SparkSession | Entry Point to Spark

// Spark SQL
df.createOrReplaceTempView("sample_table")
val df2 = spark.sql("SELECT _1,_2 FROM sample_table")
df2.show()
