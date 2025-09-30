# Example 02 from: PySpark Convert String to Array Column

# Import
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
         .appName('SparkByExamples.com') \
         .getOrCreate()

# Data
data = [("James, A, Smith","2018","M",3000),
            ("Michael, Rose, Jones","2010","M",4000),
            ("Robert,K,Williams","2010","M",4000),
            ("Maria,Anne,Jones","2005","F",4000),
            ("Jen,Mary,Brown","2010","",-1)
            ]

columns=["name","dob_year","gender","salary"]

# Create DataFrame
df=spark.createDataFrame(data,columns)
df.printSchema()
