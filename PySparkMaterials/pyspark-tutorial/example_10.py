# Example 10 from: PySpark 4.0 Tutorial For Beginners with Examples

# Spark streaming from socket
df = spark.readStream
      .format("socket")
      .option("host","localhost")
      .option("port","9090")
      .load()
