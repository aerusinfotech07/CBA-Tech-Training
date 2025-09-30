# Example 09 from: PySpark AI (pyspark-ai) – English SDK Comprehensive Guide

# Using other LLM model
from langchain.chat_models import ChatOpenAI
from pyspark_ai import SparkAI

# Use 'gpt-3.5-turbo' (might lower output quality)
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

spark_ai = SparkAI(llm=llm, verbose=True)
