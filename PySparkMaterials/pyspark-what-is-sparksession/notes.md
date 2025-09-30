# What is SparkSession | Entry Point to Spark

---

SparkSession is a unified entry point for Spark applications; it was introduced in Spark 2.0. It acts as a connector to all Spark’s underlying functionalities, including RDDs, DataFrames, and Datasets, providing a unified interface to work with structured data processing. It is one of the very first objects you create while developing a Spark SQL application. As a Spark developer, you create a SparkSession using the SparkSession.builder() method

Advertisements

SparkSession consolidates several previously separate contexts, such as SQLContext, HiveContext, and StreamingContext, into one entry point, simplifying the interaction with Spark and its different APIs. It enables users to perform various operations like reading data from various sources, executing SQL queries, creating DataFrames and Datasets, and performing actions on distributed datasets efficiently.

For those engaging with Spark through the spark-shell CLI, the ‘spark’ variable automatically provides a default Spark Session, eliminating the need for manual creation within this context.

In this article, I’ll delve into the essence of SparkSession, how to create SparkSession object, and explore its frequently utilized methods.

What is SparkSession SparkSession was introduced in version Spark 2.0, it is an entry point to underlying Spark functionality in order to programmatically create Spark RDD, DataFrame, and DataSet. SparkSession’s object spark is the default variable available in spark-shell and it can be created programmatically using SparkSession builder pattern.

If you are looking for a PySpark explanation, please refer to how to create SparkSession in PySpark .

## 1. SparkSession Introduction

As mentioned in the beginning, SparkSession is an entry point to Spark, and creating a SparkSession instance would be the first statement you would write to program with RDD , DataFrame , and Dataset. SparkSession will be created using SparkSession.builder() builder pattern.

Before Spark 2.0, SparkContext used to be an entry point, and it’s not been completely replaced with SparkSession. Many features of SparkContext are still available and used in Spark 2.0 and later. You should also know that SparkSession internally creates SparkConfig and SparkContext with the configuration provided with SparkSession.

With Spark 2.0, a new class org.apache.spark.sql.SparkSession has been introduced, which is a combined class for all the different contexts we used to have before 2.0 (SQLContext, HiveContext, etc); hence, Spark Session can be used in the place of SQLContext, HiveContext, and other contexts.

Spark Session also includes all the APIs available in different contexts –
- SparkContext
- SQLContext
- StreamingContext
- HiveContext

How many SparkSessions can you create in an application? You can create as many SparkSession as you want in a Spark application using either SparkSession.builder() or SparkSession.newSession() . Many Spark session objects are required when you want to keep Spark tables (relational entities) logically separated.

## 2. SparkSession in spark-shell

By default, Spark shell provides spark object, which is an instance of the SparkSession class. We can directly use this object when required in spark-shell .

```

// Usage of spark variable
scala> spark.version

```

Like the Spark shell, In most of the tools, notebooks, and Azure Databricks, the environment creates a default SparkSession object for us to use, so you don’t have to worry about creating a Spark session.

### 3. How to Create SparkSession

Creating a SparkSession is fundamental as it initializes the environment required to leverage the capabilities of Apache Spark.

To create SparkSession in Scala or Python, you need to use the builder pattern method builder() and calling getOrCreate() method. It returns a SparkSession that already exists; otherwise, it creates a new SparkSession. The example below creates a SparkSession in Scala.

```

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

```

From the above code –

SparkSession.builder() – Return SparkSession.Builder class. This is a builder for SparkSession . master(), appName(), and getOrCreate() are methods of SparkSession.Builder .

master() – This allows Spark applications to connect and run in different modes (local, standalone cluster, Mesos, YARN), depending on the configuration.
- Use local[x] when running on your local laptop. x should be an integer value and should be greater than 0; this represents how many partitions it should create when using RDD, DataFrame, and Dataset. Ideally, x value should be the number of CPU cores you have.
- For standalone use spark://master:7077

appName() – Sets a name to the Spark application that shows in the Spark web UI . If no application name is set, it sets a random name.

getOrCreate() – This returns a SparkSession object if it already exists. Creates a new one if it does not exist.

### 3.1 Get Existing SparkSession

You can get the existing SparkSession in Scala programmatically using the example below. To get the existing SparkSession, you don’t have to specify the app name, master e.t.c

```

// Get existing SparkSession 
import org.apache.spark.sql.SparkSession
val spark2 = SparkSession.builder().getOrCreate()
print(spark2)

// Output:
// org.apache.spark.sql.SparkSession@2fdf17dc

```

Compare the hash of spark and spark2 object. Since it returned the existing session, both objects have the same hash value.

### 3.2 Create Another SparkSession

Sometimes, you might be required to create multiple sessions, which you can easily achieve by using newSession() method. This uses the same app name and master as the existing session. Underlying SparkContext will be the same for both sessions, as you can have only one context per Spark application.

```

// Create a new SparkSession
val spark3 = spark.newSession()
print(spark3)

// Output:
// org.apache.spark.sql.SparkSession@692dba54

```

Compare this hash with the hash from the above example; it should be different.

### 3.3 Setting Spark Configs

If you want to set some configs to SparkSession, use the config() method.

```

// Usage of config()
val spark = SparkSession.builder()
      .master("local[1]")
      .appName("SparkByExamples.com")
      .config("spark.some.config.option", "config-value")
      .getOrCreate();

```

### 3.4 Create SparkSession with Hive Enable

To use Hive with Spark , you need to enable it using the enableHiveSupport () method. SparkSession from Spark2.0 provides inbuilt support for Hive operations like writing queries on Hive tables using HQL, accessing to Hive UDFs, and reading data from Hive tables.

```

// Enabling Hive to use in Spark
val spark = SparkSession.builder()
      .master("local[1]")
      .appName("SparkByExamples.com")
      .config("spark.sql.warehouse.dir", "<path>/spark-warehouse")
      .enableHiveSupport()
      .getOrCreate();

```

## 4. Other Usages of SparkSession

### 4.1 Set & Get All Spark Configs

Once the SparkSession is created, you can add the spark configs during runtime or get all configs.

```

// Set Config
spark.conf.set("spark.sql.shuffle.partitions", "30")

// Get all Spark Configs
val configMap:Map[String, String] = spark.conf.getAll

```

### 4.2 Create DataFrame

SparkSession also provides several methods to create a Spark DataFrame and Dataset. The below example uses the createDataFrame() method which takes a list of data.

```

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

```

### 4.3 Working with Spark SQL

Using SparkSession you can access Spark SQL capabilities in Apache Spark. In order to use SQL features first, you need to create a temporary view in Spark . Once you have a temporary view you can run any ANSI SQL queries using spark.sql() method.

```

// Spark SQL
df.createOrReplaceTempView("sample_table")
val df2 = spark.sql("SELECT _1,_2 FROM sample_table")
df2.show()

```

Spark SQL temporary views are session-scoped and will not be available if the session that creates it terminates. If you want to have a temporary view that is shared among all sessions and kept alive until the Spark application terminates, you can create a global temporary view using createGlobalTempView() .

### 4.4 Create Hive Table

As explained above, SparkSession can also be used to create Hive tables and query them. Note that in order to do this for testing you don’t need Hive to be installed. saveAsTable() creates Hive managed table. Query the table using spark.sql() .

```

// Create Hive table & query it.  
spark.table("sample_table").write.saveAsTable("sample_hive_table")
val df3 = spark.sql("SELECT _1,_2 FROM sample_hive_table")
df3.show()

```

### 4.5 Working with Catalogs

To get the catalog metadata, Spark Session exposes catalog variable. Note that these methods spark.catalog.listDatabases and spark.catalog.listTables returns the Dataset.

```

// Get metadata from the Catalog
// List databases
val ds = spark.catalog.listDatabases
ds.show(false)

// Output:
// +-------+----------------+----------------------------+
// |name   |description     |locationUri                 |
// +-------+----------------+----------------------------+
// |default|default database|file:/<path>/spark-warehouse|
// +-------+----------------+----------------------------+

// List Tables
val ds2 = spark.catalog.listTables
ds2.show(false)

// Output:
// +-----------------+--------+-----------+---------+-----------+
// |name             |database|description|tableType|isTemporary|
// +-----------------+--------+-----------+---------+-----------+
// |sample_hive_table|default |null       |MANAGED  |false      |
// |sample_table     |null    |null       |TEMPORARY|true       |
// +-----------------+--------+-----------+---------+-----------+

```

Notice the two tables we have created so far, The sample_table which was created from Spark.createOrReplaceTempView is considered a temporary table and Hive table as managed table .

## 5. SparkSession Commonly Used Methods
MethodDescription`version`ReturnsSpark versionwhere your application is running, probably the Spark version your cluster is configured with.`catalog`Returns the catalog object to access metadata.`conf`Returns the RuntimeConfig object.`builder()`builder() is used to create a new SparkSession, this return`SparkSession.Builder``newSession()`Creaetes a new SparkSession.`range(n)`Returns a single columnDatasetwith`LongType`and column named`id`, containing elements in a range from 0 to`n`(exclusive) with step value 1. There are several variations of this function, for details, refer to Spark documentation.`createDataFrame()`Thiscreates a DataFramefrom a collection and anRDD`createDataset()`Thiscreates a Datasetfrom the collection, DataFrame, and RDD.`emptyDataset()`Creates anempty Dataset.`getActiveSession()`Returns an active Spark session for the current thread.`getDefaultSession()`Returns the default SparkSession that is returned by the builder.`implicits()`To access the nested Scala object.`read()`Returns an instance of`DataFrameReader`class, this is used to read records from CSV, Parquet, Avro, and more file formats into DataFrame.`readStream()`Returns an instance of`DataStreamReader`class, this is used to read streaming data. that can be used to read streaming data into DataFrame.`sparkContext()`Returns aSparkContext.`sql(String sql)`Returns a DataFrame after executing the SQL mentioned.`sqlContext()`ReturnsSQLContext.`stop()`Stop the currentSparkContext.`table()`Returns a DataFrame of a table or view.`udf()`Creates aSpark UDF to use it on DataFrame, Dataset, and SQL.SparkSession Methods
## 6. FAQ’s on SparkSession

How to create SparkSession? SparkSession is created using SparkSession.builder().master("master-details").appName("app-name").getOrCreate(); Here, getOrCreate() method returns SparkSession if already exists. If not, it creates a new SparkSession. How many SparkSessions can I create? You can create as many SparkSession as you want in a Spark application using either SparkSession.builder() or SparkSession.newSession() . Many Spark session objects are required when you want to keep Spark tables (relational entities) logically separated. How to stop SparkSession? To stop SparkSession in Apache Spark, you can use the stop() method of the SparkSession object. If you have spark as a SparkSession object then call spark.stop() to stop the session. Calling a stop() is important to do when you’re finished with your Spark application. This ensures that resources are properly released and the Spark application terminates gracefully. How SparkSession is different from SparkContext? SparkSession and SparkContext are two core components of Apache Spark. Though they sound similar, they serve different purposes and are used in different contexts within a Spark application. SparkContext provides the connection to a Spark cluster and is responsible for coordinating and distributing the operations on that cluster. SparkContext is used for low-level RDD (Resilient Distributed Dataset) programming. SparkSession was introduced in Spark 2.0 to provide a more convenient and unified API for working with structured data. It’s designed to work with DataFrames and Datasets, which provide more structured and optimized operations than RDDs. Do we need to stop SparkSession? It is recommended to end the Spark session after finishing the Spark job in order for the JVMs to close and free the resources. How do I know if my Spark session is active? To check if your SparkSession is active, you can use the SparkSession object’s sparkContext attribute and check its isActive property. If you have spark as a SparkSession object then call spark.sparkContext.isActive . This returns true if it is active otherwise false.

## 7. Conclusion

In this Spark SparkSession article, you have learned what is Spark Session, its usage, how to create SparkSession programmatically, and learned some of the commonly used SparkSession methods. In summary
- SparkSession was introduced in Spark 2.0 which is a unified API for working with structured data.
- It combines SparkContext , SQLContext, and HiveContext. It’s designed to work with DataFrames and Datasets, which provide more structured and optimized operations than RDDs.
- SparkSession natively supports SQL queries, structured streaming, and DataFrame-based machine learning APIs.
- spark-shell, Databricks, and other tools provide spark variable as the default SparkSession object.

Happy Learning !!

## Related Articles
- How to resolve NameError: Name ‘Spark’ is not Defined?
- How to resolve Spark Context ‘sc’ Not Defined?
- SparkSession vs SQLContext
- Spark – Create a SparkSession and SparkContext
- SparkSession vs SparkContext
- Spark Set JVM Options to Driver & Executors
- Spark Set Environment Variable to Executors

## Reference
- https://spark.apache.org/docs/1.6.1/sql-programming-guide.html#starting-point-sqlcontext

