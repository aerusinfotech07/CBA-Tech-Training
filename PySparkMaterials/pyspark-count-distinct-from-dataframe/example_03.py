# Example 03 from: PySpark Count Distinct from DataFrame

df.createOrReplaceTempView("EMP")
spark.sql("select distinct(count(*)) from EMP").show()

# Displays this on console
+--------+
|count(1)|
+--------+
|      10|
+--------+
