# Example 06 from: Pandas API on Spark | Explained With Examples

# Pandas API on Spark Dataframe into a Spark DataFrame
sdf = df.to_spark()
print(type(sdf))
sdf.show()

# Output
#<class 'pyspark.sql.dataframe.DataFrame'>
#+-------+-----+--------+--------+
#|Courses|  Fee|Duration|Discount|
#+-------+-----+--------+--------+
#|  Spark|22000|  30days|  1000.0|
#|PySpark|25000|  50days|  2300.0|
#| Hadoop|23000|  55days|  1000.0|
#| Python|24000|  40days|  1200.0|
#| Pandas|26000|  60days|  2500.0|
#| Hadoop|25000|  35days|    null|
#|  Spark|25000|  30days|  1400.0|
#| Python|22000|  50days|  1600.0|
#|     NA| 1500|  40days|     0.0|
#+-------+-----+--------+--------+
