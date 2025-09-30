# Example 02 from: PySpark foreach() Usage with Examples

# foreach() with accumulator Example
accum=spark.sparkContext.accumulator(0)
df.foreach(lambda x:accum.add(int(x.Seqno)))
print(accum.value) #Accessed by driver
