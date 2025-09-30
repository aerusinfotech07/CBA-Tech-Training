# Example 02 from: PySpark Read and Write MySQL Database Table

# Read from MySQL Table
val df = spark.read \
    .format("jdbc") \
    .option("driver","com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://localhost:3306/emp") \
    .option("dbtable", "employee") \
    .option("user", "root") \
    .option("password", "root") \
    .load()
