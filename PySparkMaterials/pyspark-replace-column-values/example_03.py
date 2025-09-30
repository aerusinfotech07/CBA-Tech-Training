# Example 03 from: PySpark Replace Column Values in DataFrame

#Replace string column value conditionally
from pyspark.sql.functions import when
df.withColumn('address', 
    when(df.address.endswith('Rd'),regexp_replace(df.address,'Rd','Road')) \
   .when(df.address.endswith('St'),regexp_replace(df.address,'St','Street')) \
   .when(df.address.endswith('Ave'),regexp_replace(df.address,'Ave','Avenue')) \
   .otherwise(df.address)) \
   .show(truncate=False)

#+---+----------------------+-----+
#|id |address               |state|
#+---+----------------------+-----+
#|1  |14851 Jeffrey Road    |DE   |
#|2  |43421 Margarita Street|NY   |
#|3  |13111 Siemon Avenue   |CA   |
#+---+----------------------+-----+
