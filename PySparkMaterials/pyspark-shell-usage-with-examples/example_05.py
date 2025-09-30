# Example 05 from: PySpark Shell Command Usage with Examples

./bin/pyspark \
   --master yarn \
   --deploy-mode cluster \
   --driver-memory 8g \
   --executor-memory 16g \
   --executor-cores 2  \
   --conf "spark.sql.shuffle.partitions=20000" \
   --conf "spark.executor.memoryOverhead=5244" \
   --conf "spark.memory.fraction=0.8" \
   --conf "spark.memory.storageFraction=0.2" \
   --py-files file1.py,file2.py
