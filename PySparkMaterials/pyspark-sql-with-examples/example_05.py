# Example 05 from: PySpark SQL Tutorial with Examples

# SQL where
spark.sql(""" SELECT  country, city, zipcode, state FROM ZIPCODES 
          WHERE state = 'AZ' """) \
     .show(5)
