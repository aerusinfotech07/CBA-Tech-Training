# Example 06 from: PySpark Read and Write Parquet File

parDF2=spark.read.parquet("/tmp/output/people2.parquet/gender=M")
parDF2.show(truncate=False)
