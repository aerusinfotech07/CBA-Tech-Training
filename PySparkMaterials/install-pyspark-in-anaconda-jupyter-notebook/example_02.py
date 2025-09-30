# Example 02 from: Install PySpark in Anaconda & Jupyter Notebook

# Create DataFrame in PySpark Shell
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
df = spark.createDataFrame(data)
df.show()
