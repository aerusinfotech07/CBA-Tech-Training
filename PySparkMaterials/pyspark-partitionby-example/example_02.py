# Example 02 from: PySpark partitionBy() – Write to Disk Example

# Reading from partitioned data
dfSinglePart=spark.read.option("header",True) \
            .csv("c:/tmp/zipcodes-state/state=AL/city=SPRINGVILLE")
dfSinglePart.printSchema()
dfSinglePart.show()

#Displays
root
 |-- RecordNumber: string (nullable = true)
 |-- Country: string (nullable = true)
 |-- Zipcode: string (nullable = true)

+------------+-------+-------+
|RecordNumber|Country|Zipcode|
+------------+-------+-------+
|       54355|     US|  35146|
+------------+-------+-------+
