# Example 02 from: PySpark to_date() – Convert Timestamp to Date

from pyspark.sql.functions import *

#Timestamp String to DateType
df.withColumn("date_type",to_date("input_timestamp")) \
  .show(truncate=False)

#Timestamp Type to DateType
df.withColumn("date_type",to_date(current_timestamp())) \
  .show(truncate=False) 

#Above Both examples display
+---+-----------------------+----------+
|id |input_timestamp        |date_type |
+---+-----------------------+----------+
|1  |2019-06-24 12:01:19.000|2019-06-24|
+---+-----------------------+----------+

#Custom Timestamp format to DateType
df.select(to_date(lit('06-24-2019 12:01:19.000'),'MM-dd-yyyy HH:mm:ss.SSSS')) \
  .show()

#Displays
+--------------------------------------------------------------+
|to_date('06-24-2019 12:01:19.000', 'MM-dd-yyyy HH:mm:ss.SSSS')|
+--------------------------------------------------------------+
|                                                    2019-06-24|
+--------------------------------------------------------------+
