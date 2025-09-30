# Example 02 from: PySpark SQL Tutorial with Examples

# Read CSV file into table
df = spark.read.option("header",True) \
          .csv("/Users/admin/simple-zipcodes.csv")
df.printSchema()
df.show()
