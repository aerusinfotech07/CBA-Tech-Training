# Example 03 from: PySpark Read and Write Parquet File

# Read parquet file using read.parquet()
parDF=spark.read.parquet("/tmp/output/people.parquet")
