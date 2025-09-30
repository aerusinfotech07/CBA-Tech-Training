# Example 04 from: PySpark SQL Read Hive Table

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
