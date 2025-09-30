# Example 04 from: PySpark SQL Tutorial with Examples

# SQL Select query
spark.sql("SELECT country, city, zipcode, state FROM ZIPCODES") \
     .show(5)
