# Example 03 from: PySpark Read and Write MySQL Database Table

# Read from SQL Table
df = spark.read \ 
  .format("jdbc") \
  .option("driver","com.mysql.cj.jdbc.Driver") \
  .option("url", "jdbc:mysql://localhost:3306/emp") \
  .option("dbtable", "select id,age from employee where gender='M'") \
  .option("user", "root") \
  .option("password", "root") \
  .load()

df.show()
