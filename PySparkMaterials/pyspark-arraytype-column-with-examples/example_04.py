# Example 04 from: PySpark ArrayType Column With Examples

from pyspark.sql.functions import split
df.select(split(df.name,",").alias("nameAsArray")).show()

+--------------------+
|         nameAsArray|
+--------------------+
|    [James, , Smith]|
|   [Michael, Rose, ]|
|[Robert, , Williams]|
+--------------------+
