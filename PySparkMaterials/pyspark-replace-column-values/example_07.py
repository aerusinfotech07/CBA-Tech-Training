# Example 07 from: PySpark Replace Column Values in DataFrame

#Overlay
from pyspark.sql.functions import overlay
df = spark.createDataFrame([("ABCDE_XYZ", "FGH")], ("col1", "col2"))
df.select(overlay("col1", "col2", 7).alias("overlayed")).show()

#+---------+
#|overlayed|
#+---------+
#|ABCDE_FGH|
#+---------+
