# Example 05 from: PySpark Replace Column Values in DataFrame

#Using translate to replace character by character
from pyspark.sql.functions import translate
df.withColumn('address', translate('address', '123', 'ABC')) \
  .show(truncate=False)

#+---+------------------+-----+
#|id |address           |state|
#+---+------------------+-----+
#|1  |A485A Jeffrey Rd  |DE   |
#|2  |4C4BA Margarita St|NY   |
#|3  |ACAAA Siemon Ave  |CA   |
#+---+------------------+-----+
