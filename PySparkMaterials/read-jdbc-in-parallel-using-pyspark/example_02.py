# Example 02 from: Read JDBC in Parallel using PySpark

# Read Table in Parallel
df = spark.read \
    .format("jdbc") \
    .option("driver","com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://localhost:3306/emp") \
    .option("dbtable","employee") \
    .option("numPartitions",5) \
    .option("user", "root") \
    .option("password", "root") \
    .load()
