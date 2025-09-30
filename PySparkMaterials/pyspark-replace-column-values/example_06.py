# Example 06 from: PySpark Replace Column Values in DataFrame

#Replace column with another column
from pyspark.sql.functions import expr
df = spark.createDataFrame(
   [("ABCDE_XYZ", "XYZ","FGH")], 
    ("col1", "col2","col3")
  )
df.withColumn("new_column",
              expr("regexp_replace(col1, col2, col3)")
              .alias("replaced_value")
              ).show()

#+---------+----+----+----------+
#|     col1|col2|col3|new_column|
#+---------+----+----+----------+
#|ABCDE_XYZ| XYZ| FGH| ABCDE_FGH|
#+---------+----+----+----------+
