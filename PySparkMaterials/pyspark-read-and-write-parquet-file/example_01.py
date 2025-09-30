# Example 01 from: PySpark Read and Write Parquet File

# Read and Write Parquet file using parquet()
df.write.parquet("/tmp/out/people.parquet") 
parDF1=spark.read.parquet("/temp/out/people.parquet")
