# Example 02 from: What is SparkSession | Entry Point to Spark

// Create SparkSession object
import org.apache.spark.sql.SparkSession
object SparkSessionTest extends App {
  val spark = SparkSession.builder()
      .master("local[1]")
      .appName("SparkByExamples.com")
      .getOrCreate();
  println(spark)
  println("Spark Version : "+spark.version)
}

// Outputs
// org.apache.spark.sql.SparkSession@2fdf17dc
// Spark Version : 3.4.1
