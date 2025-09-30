# Example 03 from: PySpark partitionBy() – Write to Disk Example

# Read from partitioned data using sql
parqDF = spark.read.option("header",True) \
                  .csv("/tmp/zipcodes-state")
parqDF.createOrReplaceTempView("ZIPCODE")
spark.sql("select * from ZIPCODE  where state='AL' and city = 'SPRINGVILLE'") \
    .show()

#Display
+------------+-------+-------+-----+-----------+
|RecordNumber|Country|Zipcode|state|       city|
+------------+-------+-------+-----+-----------+
|       54355|     US|  35146|   AL|SPRINGVILLE|
+------------+-------+-------+-----+-----------+
