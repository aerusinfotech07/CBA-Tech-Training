# Example 03 from: PySpark DataFrame groupBy and Sort by Descending Order

df.createOrReplaceTempView("EMP")
spark.sql("select state, sum(salary) as sum_salary from EMP " +
          "group by state having sum_salary > 100000 " + 
          "order by sum_salary desc").show()
