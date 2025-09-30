# Example 05 from: PySpark ArrayType Column With Examples

from pyspark.sql.functions import array
df.select(df.name,array(df.currentState,df.previousState).alias("States")).show()
+----------------+--------+
|            name|  States|
+----------------+--------+
|    James,,Smith|[OH, CA]|
|   Michael,Rose,|[NY, NJ]|
|Robert,,Williams|[UT, NV]|
+----------------+--------+
