# Example 02 from: PySpark Query Database Table using JDBC

# Query from MySQL Table
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/emp") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "employee") \
    .option("user", "root") \
    .option("password", "root") \
    .load()
