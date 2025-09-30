# Example 04 from: PySpark SQL expr() (Expression) Function

# Providing alias using 'as'
from pyspark.sql.functions import expr
df.select(df.date,df.increment,
     expr("""add_months(date,increment) as inc_date""")
  ).show()
# This yields same output as above
