# Example 04 from: PySpark Groupby Explained with Example

# Register DataFrame as a temporary view
df.createOrReplaceTempView("employees")

# Using SQL Query
sql_string = """SELECT department,
       SUM(salary) AS sum_salary,
       AVG(salary) AS avg_salary,
       SUM(bonus) AS sum_bonus,
       MAX(bonus) AS max_bonus
FROM employees
GROUP BY department
HAVING SUM(bonus) >= 50000"""

# Execute SQL query against the temporary view
df2 = spark.sql(sql_string)
df2.show()
