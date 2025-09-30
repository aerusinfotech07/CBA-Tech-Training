# Example 03 from: Read JDBC in Parallel using PySpark

# Select columns with where clause
df = spark.read \
    .format("jdbc") \
    .option("driver","com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://localhost:3306/emp") \
    .option("query","select id,age from employee where gender='M'") \
    .option("numPartitions",5) \
    .option("user", "root") \
    .option("password", "root") \
    .load()
