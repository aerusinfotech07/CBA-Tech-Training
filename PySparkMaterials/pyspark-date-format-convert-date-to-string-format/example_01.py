# Example 01 from: PySpark date_format() – Convert Date to String format

# Import
from pyspark.sql.functions import *

# Create DataFrame
df=spark.createDataFrame([["1"]],["id"])

# Using date_format()
df.select(current_date().alias("current_date"), \
      date_format(current_timestamp(),"yyyy MM dd").alias("yyyy MM dd"), \
      date_format(current_timestamp(),"MM/dd/yyyy hh:mm").alias("MM/dd/yyyy"), \
      date_format(current_timestamp(),"yyyy MMM dd").alias("yyyy MMMM dd"), \
      date_format(current_timestamp(),"yyyy MMMM dd E").alias("yyyy MMMM dd E") \
   ).show()
