# Example 06 from: PySpark SQL Tutorial with Examples

# SQL ORDER BY
spark.sql(""" SELECT  country, city, zipcode, state FROM ZIPCODES 
          WHERE state in ('PR','AZ','FL') order by state """) \
     .show(10)
