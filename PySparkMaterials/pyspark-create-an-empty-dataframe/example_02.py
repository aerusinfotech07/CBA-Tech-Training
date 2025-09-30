# Example 02 from: PySpark – Create an Empty DataFrame & RDD

#Creates Empty RDD using parallelize
rdd2= spark.sparkContext.parallelize([])
print(rdd2)

#EmptyRDD[205] at emptyRDD at NativeMethodAccessorImpl.java:0
#ParallelCollectionRDD[206] at readRDDFromFile at PythonRDD.scala:262
