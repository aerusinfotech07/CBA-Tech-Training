# Example 06 from: What is SparkSession | Entry Point to Spark

// Enabling Hive to use in Spark
val spark = SparkSession.builder()
      .master("local[1]")
      .appName("SparkByExamples.com")
      .config("spark.sql.warehouse.dir", "<path>/spark-warehouse")
      .enableHiveSupport()
      .getOrCreate();
