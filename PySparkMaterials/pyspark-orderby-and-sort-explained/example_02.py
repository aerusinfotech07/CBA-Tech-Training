# Example 02 from: PySpark orderBy() and sort() explained

# Sort using spark SQL

df.createOrReplaceTempView("EMP")
spark.sql("select employee_name,department,state,salary,age,bonus from EMP ORDER BY department asc").show(truncate=False)
