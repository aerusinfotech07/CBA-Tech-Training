# Example 02 from: PySpark Random Sample with Example

rdd = spark.sparkContext.range(0,100)
print(rdd.sample(False,0.1,0).collect())
//Output: [24, 29, 41, 64, 86]
print(rdd.sample(True,0.3,123).collect())
//Output: [0, 11, 13, 14, 16, 18, 21, 23, 27, 31, 32, 32, 48, 49, 49, 53, 54, 72, 74, 77, 77, 83, 88, 91, 93, 98, 99]
