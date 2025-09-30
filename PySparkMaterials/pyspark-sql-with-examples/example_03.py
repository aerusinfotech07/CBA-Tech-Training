# Example 03 from: PySpark SQL Tutorial with Examples

# Create temporary table
spark.read.option("header",True) \
          .csv("/Users/admin/simple-zipcodes.csv") \
          .createOrReplaceTempView("Zipcodes")
