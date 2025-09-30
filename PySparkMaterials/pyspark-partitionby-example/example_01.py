# Example 01 from: PySpark partitionBy() – Write to Disk Example

# Create DataFrame by reading CSV file
df=spark.read.option("header",True) \
        .csv("/tmp/resources/simple-zipcodes.csv")
df.printSchema()

#Display below schema
root
 |-- RecordNumber: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- City: string (nullable = true)
 |-- Zipcode: string (nullable = true)
 |-- state: string (nullable = true)
