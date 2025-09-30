# Example 08 from: PySpark AI (pyspark-ai) – English SDK Comprehensive Guide

from pyspark.sql import SparkSession
import pandas as pd
import plotly.express as px

# Start Spark session
spark = SparkSession.builder.getOrCreate()

# Assuming df is the DataFrame
# Aggregate the data
df_agg = df.groupBy('state', 'country').sum('total_salary')

# Convert to pandas DataFrame
df_pd = df_agg.toPandas()

# Plot the data
fig = px.bar(df_pd, x='state', y='sum(total_salary)', color='country', title='Total Salary by State and Country')
fig.show()
