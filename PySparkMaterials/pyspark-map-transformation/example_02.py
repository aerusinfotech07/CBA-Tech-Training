# Example 02 from: PySpark map() Transformation

data = [('James','Smith','M',30),
  ('Anna','Rose','F',41),
  ('Robert','Williams','M',62), 
]

columns = ["firstname","lastname","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()

# Output:
#+---------+--------+------+------+
#|firstname|lastname|gender|salary|
#+---------+--------+------+------+
#|    James|   Smith|     M|    30|
#|     Anna|    Rose|     F|    41|
#|   Robert|Williams|     M|    62|
#+---------+--------+------+------+
