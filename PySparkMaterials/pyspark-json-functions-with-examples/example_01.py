# Example 01 from: PySpark JSON Functions with Examples

from pyspark.sql import SparkSession,Row
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

jsonString="""{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}"""
df=spark.createDataFrame([(1, jsonString)],["id","value"])
df.show(truncate=False)

//+---+--------------------------------------------------------------------------+
//|id |value                                                                     |
//+---+--------------------------------------------------------------------------+
//|1  |{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}|
//+---+--------------------------------------------------------------------------+
