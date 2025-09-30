# Example 01 from: PySpark SQL Read Hive Table

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
