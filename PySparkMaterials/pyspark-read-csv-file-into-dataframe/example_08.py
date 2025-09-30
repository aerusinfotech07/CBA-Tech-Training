# Example 08 from: PySpark Read CSV file into DataFrame

# Define read options
options = {
    "inferSchema": "True",
    "delimiter": ","
}

# Read a CSV file with specified options
df4 = spark.read.options(**options).csv("/path/zipcodes.csv")
