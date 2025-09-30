# Example 01 from: PySpark Repartition() vs Coalesce()

# Create spark session with local[5]
rdd = spark.sparkContext.parallelize(range(0,20))
print("From local[5] : "+str(rdd.getNumPartitions()))

# Use parallelize with 6 partitions
rdd1 = spark.sparkContext.parallelize(range(0,25), 6)
print("parallelize : "+str(rdd1.getNumPartitions()))

rddFromFile = spark.sparkContext.textFile("src/main/resources/test.txt",10)
print("TextFile : "+str(rddFromFile.getNumPartitions()))
