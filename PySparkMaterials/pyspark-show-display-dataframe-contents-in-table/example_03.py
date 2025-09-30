# Example 03 from: PySpark show() – Display DataFrame Contents in Table

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
columns = ["Seqno","Quote"]
data = [("1", "Be the change that you wish to see in the world"),
    ("2", "Everyone thinks of changing the world, but no one thinks of changing himself."),
    ("3", "The purpose of our lives is to be happy."),
    ("4", "Be cool.")]
df = spark.createDataFrame(data,columns)
df.show()

# Output
#+-----+--------------------+
#|Seqno|               Quote|
#+-----+--------------------+
#|    1|Be the change tha...|
#|    2|Everyone thinks o...|
#|    3|The purpose of ou...|
#|    4|            Be cool.|
#+-----+--------------------+
