# Example 07 from: PySpark SQL Tutorial with Examples

# SQL GROUP BY clause
spark.sql(""" SELECT state, count(*) as count FROM ZIPCODES 
          GROUP BY state""") \
     .show()
