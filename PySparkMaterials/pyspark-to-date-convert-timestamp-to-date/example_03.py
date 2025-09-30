# Example 03 from: PySpark to_date() – Convert Timestamp to Date

#SQL TimestampType to DateType
spark.sql("select to_date(current_timestamp) as date_type")

#SQL CAST TimestampType to DateType
spark.sql("select date(to_timestamp('2019-06-24 12:01:19.000')) as date_type")

#SQL CAST timestamp string to DateType
spark.sql("select date('2019-06-24 12:01:19.000') as date_type")

#SQL Timestamp String (default format) to DateType
spark.sql("select to_date('2019-06-24 12:01:19.000') as date_type")

#SQL Custom Timeformat to DateType
spark.sql("select to_date('06-24-2019 12:01:19.000','MM-dd-yyyy HH:mm:ss.SSSS') as date_type")
