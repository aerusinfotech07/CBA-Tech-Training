# Example 05 from: What is SparkSession | Entry Point to Spark

// Usage of config()
val spark = SparkSession.builder()
      .master("local[1]")
      .appName("SparkByExamples.com")
      .config("spark.some.config.option", "config-value")
      .getOrCreate();
