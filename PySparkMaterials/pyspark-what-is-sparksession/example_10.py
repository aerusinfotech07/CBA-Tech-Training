# Example 10 from: What is SparkSession | Entry Point to Spark

// Create Hive table & query it.  
spark.table("sample_table").write.saveAsTable("sample_hive_table")
val df3 = spark.sql("SELECT _1,_2 FROM sample_hive_table")
df3.show()
