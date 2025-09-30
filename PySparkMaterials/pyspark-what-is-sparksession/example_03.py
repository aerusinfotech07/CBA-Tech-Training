# Example 03 from: What is SparkSession | Entry Point to Spark

// Get existing SparkSession 
import org.apache.spark.sql.SparkSession
val spark2 = SparkSession.builder().getOrCreate()
print(spark2)

// Output:
// org.apache.spark.sql.SparkSession@2fdf17dc
