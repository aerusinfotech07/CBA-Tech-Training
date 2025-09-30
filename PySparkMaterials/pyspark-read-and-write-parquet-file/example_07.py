# Example 07 from: PySpark Read and Write Parquet File

# Create a temporary view on partitioned Parquet file
spark.sql("CREATE TEMPORARY VIEW PERSON2 USING parquet OPTIONS (path \"/tmp/output/people2.parquet/gender=F\")")
spark.sql("SELECT * FROM PERSON2" ).show()
