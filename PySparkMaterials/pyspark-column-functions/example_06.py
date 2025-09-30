# Example 06 from: PySpark Column Class | Operators & Functions

#alias
from pyspark.sql.functions import expr
df.select(df.fname.alias("first_name"), \
          df.lname.alias("last_name")
   ).show()

#Another example
df.select(expr(" fname ||','|| lname").alias("fullName") \
   ).show()
