# Example 11 from: What is SparkSession | Entry Point to Spark

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
