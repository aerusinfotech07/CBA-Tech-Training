# Example 08 from: PySpark RDD Tutorial | Learn with Examples

# persist()
import pyspark
dfPersist = rdd.persist(pyspark.StorageLevel.MEMORY_ONLY)
dfPersist.show(false)
