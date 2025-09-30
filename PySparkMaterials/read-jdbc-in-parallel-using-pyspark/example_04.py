# Example 04 from: Read JDBC in Parallel using PySpark

# Using fetchsize
df = spark.read \
    .format("jdbc") \
    .option("driver","com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://localhost:3306/emp") \
    .option("query","select id,age from employee where gender='M'") \
    .option("numPartitions",5) \
    .option("fetchsize", 20) \
    .option("user", "root") \
    .option("password", "root") \
    .load()
