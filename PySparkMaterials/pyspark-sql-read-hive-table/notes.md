# PySpark SQL Read Hive Table

---

How to read or query a Hive table into PySpark DataFrame? PySpark SQL supports reading a Hive table to DataFrame in two ways: the SparkSesseion.read.table() method and the SparkSession.sql() statement.

Advertisements

To read a Hive table, you need to create a SparkSession with enableHiveSupport() . This method is available at pyspark.sql.SparkSession.builder.enableHiveSupport() which is used to enable Hive support, including connectivity to a persistent Hive metastore, support for Hive SerDes, and Hive user-defined functions.

Steps to Read Hive Table into PySpark DataFrame
- Step 1 – Import PySpark
- Step 2 – Create SparkSession with Hive enabled
- Step 3 – Query Hive table using spark.sql()
- Step 4 – Read using spark.read.table()
- Step 5 – Connect to remove Hive.

## 1. Create Spark Session with Hive Enabled

In order to read the hive table into pySpark DataFrame first, you need to create a SparkSession with Hive support enabled. In case you wanted to read from remove hive cluster refer to How to connect Remote Hive Cluster from Spark .

```

from os.path import abspath
from pyspark.sql import SparkSession

#enableHiveSupport() -> enables sparkSession to connect with Hive
warehouse_location = abspath('spark-warehouse')
spark = SparkSession \
    .builder \
    .appName("SparkByExamples.com") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

```

PySpark reads the data from the default Hive warehouse location which is /user/hive/warehouse when you use a Hive cluster. But on local, it reads from the current directory. You can change this behavior using the spark.sql.warehouse.dir configuration while creating a SparkSession .

## 2. PySpark Read or Query Hive Table into DataFrame

In my previous article, I saved a Hive table from PySpark DataFrame , which created Hive files at the default location, which is inside the spark-warehouse directory within the current directory.

Let’s read the Hive table into PySpark DataFrame.

```

# Read Hive table
df = spark.sql("select * from emp.employee")
df.show()

```

Yields the below output.

pyspark read hive table

## 3. Using spark.read.table()

Alternatively, you can also read by using spark.read.table() method. here, spark.read is an object of the class DataFrameReader.

```

# Read Hive table
df = spark.read.table("employee")
df.show()

```

## 4. PySpark Read Hive Table from Remote Hive

```

from os.path import abspath
from pyspark.sql import SparkSession

#enableHiveSupport() -> enables sparkSession to connect with Hive
warehouse_location = abspath('spark-warehouse')
spark = SparkSession \
    .builder \
    .appName("SparkByExamples.com") \
    .config("spark.sql.warehouse.dir", "/hive/warehouse/dir") \
    .config("hive.metastore.uris", "thrift://remote-host:9083") \
    .enableHiveSupport() \
    .getOrCreate()

# or Use the below approach
# Change using conf
spark.sparkContext().conf().set("spark.sql.warehouse.dir", "/user/hive/warehouse");
spark.sparkContext().conf().set("hive.metastore.uris", "thrift://localhost:9083");

```

## 5. Conclusion

In this article, you have learned how to read the Hive table into Spark DataFrame by creating SparkSession with enableHiveSupport() and using the dependencies required to connect to the Hive. Also, learned how to read by using SparkSesseion.read.table() method and the SparkSession.sql() .

You can find the complete working example at GitHub PySpark Hive Example

## Related Articles
- PySpark Read and Write MySQL Database Table
- PySpark Read JDBC Table to DataFrame
- PySpark createOrReplaceTempView() Explained
- PySpark Save DataFrame to Hive Table
- PySpark Read and Write SQL Server Table
- Pandas API on Spark | Explained With Examples
- PySpark SQL expr() (Expression ) Function
- PySpark SQL Date and Timestamp Functions

