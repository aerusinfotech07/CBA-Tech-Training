# PySpark Write to CSV File

---

In PySpark you can save (write/extract) a DataFrame to a CSV file on disk by using dataframeObj.write.csv("path") , using this you can also write DataFrame to AWS S3, Azure Blob, HDFS, or any PySpark supported file systems.

Advertisements

In this article, I will explain how to write a PySpark write CSV file to disk, S3, HDFS with or without a header, I will also cover several options like compressed, delimiter, quote, escape e.t.c and finally using different save mode options.

Since Spark 2.0.0 version CSV is natively supported without any external dependencies, if you are using an older version you would need to use databricks spark-csv library . Most of the examples and concepts explained here can also be used to write Parquet, Avro, JSON, text, ORC, and any Spark supported file formats, all you need is just replace csv() with parquet() , avro() , json() , text() , orc() respectively.

First, let’s create a DataFrame by reading a CSV file .

```
 
# Import
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.master("local[1]") \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()

# Read CSV file into DataFrame
df = spark.read.csv("/tmp/resources/zipcodes.csv")

```

## 1. DataFrameWriter.write() Syntax

Following is the syntax of the DataFrameWriter.csv() method.

```
 
# Syntax of DataFrameWriter.csv()
DataFrameWriter.csv(path, mode=None, compression=None, sep=None, quote=None, 
escape=None, header=None, nullValue=None, escapeQuotes=None, quoteAll=None, 
dateFormat=None, timestampFormat=None, ignoreLeadingWhiteSpace=None, 
ignoreTrailingWhiteSpace=None, charToEscapeQuoteEscaping=None, 
encoding=None, emptyValue=None, lineSep=None)

```

## 2. Write PySpark to CSV file

Use the write() method of the PySpark DataFrameWriter object to export PySpark DataFrame to a CSV file.

Using this you can save or write a DataFrame at a specified path on disk, this method takes a file path where you wanted to write a file and by default, it doesn’t write a header or column names.

```
 
#Write DataFrame to CSV file
df.write.csv("/tmp/spark_output/zipcodes")

```

## 3. PySpark Write to CSV with Header

In the below example I have used the option header with value True hence, it writes the DataFrame to CSV file with a column header.

```
 
# Write CSV file with column header (column names)
df.write.option("header",True) \
 .csv("/tmp/spark_output/zipcodes")

```

## 4. Write CSV Options

While writing a CSV file you can use several options. for example, header to output the DataFrame column names as header record and delimiter to specify the delimiter on the CSV output file.

```
 
# Other CSV options
df2.write.options(header='True', delimiter=',') \
 .csv("/tmp/spark_output/zipcodes")
 
```

Other options available quote , escape , nullValue , dateFormat , quoteMode .

## 5. Write Saving modes

PySpark DataFrameWriter also has a method mode() to specify saving mode.

overwrite – mode is used to overwrite the existing file.

append – To add the data to the existing file.

ignore – Ignores write operation when the file already exists.

error – This is a default option when the file already exists, it returns an error.

```
 
# Saving modes
df2.write.mode('overwrite').csv("/tmp/spark_output/zipcodes")
# You can also use this
df2.write.format("csv").mode('overwrite').save("/tmp/spark_output/zipcodes")

```

## 5. Conclusion

In this article, you have learned by using PySpark DataFrame.write() method you can write the DF to a CSV file. By default it doesn’t write the column names from the header, in order to do so, you have to use the header option with the value True.

## Related Articles
- PySpark Read CSV file into DataFrame
- PySpark Read and Write SQL Server Table
- PySpark Read and Write MySQL Database Table
- Spark/Pyspark Application Configuration
- Dynamic way of doing ETL through Pyspark
- PySpark cache() Explained.
- PySpark repartition() – Explained with Examples
- PySpark Create RDD with Examples
- PySpark printSchema() to String or JSON
- PySpark RDD Actions with examples

