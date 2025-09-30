# Example 04 from: PySpark Read and Write Parquet File

# Using spark.sql
parqDF.createOrReplaceTempView("ParquetTable")
parkSQL = spark.sql("select * from ParquetTable where salary >= 4000 ")
