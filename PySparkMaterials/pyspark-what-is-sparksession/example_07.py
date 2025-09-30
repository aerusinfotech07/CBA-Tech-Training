# Example 07 from: What is SparkSession | Entry Point to Spark

// Set Config
spark.conf.set("spark.sql.shuffle.partitions", "30")

// Get all Spark Configs
val configMap:Map[String, String] = spark.conf.getAll
