# Example 02 from: PySpark Select Columns From DataFrame

# Select columns by different ways
df.select("firstname","lastname").show()
df.select(df.firstname,df.lastname).show()
df.select(df["firstname"],df["lastname"]).show()

# By using col() function
from pyspark.sql.functions import col
df.select(col("firstname"),col("lastname")).show()

# Select columns by regular expression
df.select(df.colRegex("`^.*name*`")).show()
