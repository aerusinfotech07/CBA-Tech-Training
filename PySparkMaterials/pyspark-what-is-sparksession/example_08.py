# Example 08 from: What is SparkSession | Entry Point to Spark

// Create DataFrame
val df = spark.createDataFrame(
    List(("Scala", 25000), ("Spark", 35000), ("PHP", 21000)))
df.show()

// Output:
// +-----+-----+
// |   _1|   _2|
// +-----+-----+
// |Scala|25000|
// |Spark|35000|
// |  PHP|21000|
// +-----+-----+
