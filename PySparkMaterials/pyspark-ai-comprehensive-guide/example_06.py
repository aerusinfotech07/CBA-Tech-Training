# Example 06 from: PySpark AI (pyspark-ai) – English SDK Comprehensive Guide

# Create DataFrame from web
auto_df = spark_ai.create_df("https://www.structnet.com/instructions/zip_min_max_by_state.html")
auto_df.show()
