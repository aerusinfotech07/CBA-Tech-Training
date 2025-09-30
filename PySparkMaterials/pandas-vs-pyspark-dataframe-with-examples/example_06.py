# Example 06 from: Pandas vs PySpark DataFrame With Examples

# PySpark SQL
pysparkDF.createOrReplaceTempView("Employee")
spark.sql("select * from Employee where salary > 100000").show()

# Prints result
#+----------+-----------+---------+---+------+------+
#|first_name|middle_name|last_name|Age|gender|salary|
#+----------+-----------+---------+---+------+------+
#|    Robert|           | Williams| 42|      |400000|
#|     Maria|       Anne|    Jones| 38|     F|500000|
#+----------+-----------+---------+---+------+------+

spark.sql("select mean(age),mean(salary) from Employee").show()

# Prints result
#+---------+------------+
#|mean(age)|mean(salary)|
#+---------+------------+
#|     41.0|    206000.0|
#+---------+------------+
