# Example 03 from: PySpark transform() Function with Example

# Custom transformation 1
from pyspark.sql.functions import upper
def to_upper_str_columns(df):
    return df.withColumn("CourseName",upper(df.CourseName))

# Custom transformation 2
def reduce_price(df,reduceBy):
    return df.withColumn("new_fee",df.fee - reduceBy)

# Custom transformation 3
def apply_discount(df):
    return df.withColumn("discounted_fee",  \
             df.new_fee - (df.new_fee * df.discount) / 100)
