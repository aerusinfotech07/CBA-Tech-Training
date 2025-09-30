# Example 02 from: PySpark RDD Actions with examples

#fold
from operator import add
foldRes=listRdd.fold(0, add)
print(foldRes)
