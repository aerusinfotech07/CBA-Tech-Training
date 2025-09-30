# Example 02 from: PySpark Shell Command Usage with Examples

>>> data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
>>> df = spark.createDataFrame(data)
>>> df.show()
