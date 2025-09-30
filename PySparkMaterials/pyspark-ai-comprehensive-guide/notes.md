# PySpark AI (pyspark-ai) – English SDK Comprehensive Guide

---

Since ChatGPT release, every thing in technology is happening around AI. PySpark also released an English SDK package called pyspark-ai which allows you to write transformations in English instead of using DataFrame API or SQL. In other words, it enables you to use natural language in data processing and analysis more elegantly.

Advertisements

Using English to get the analytical results will at least eliminate you from learning DataFrame API and SQL to some extent. In this article, I will explore pyspark-ai English SDK by installing and using English instructions to apply DataFrame transformations, run some simple analytical queries, and explore the results in tables and charts.

This package makes PySpark simple and more user-friendly. You don’t have to learn to code or write complex queries and focus your effort on using the data to get insights.

## What is PySpark AI (pyspark-ai)?

PySpark AI (pyspark-ai) is a wrapper with an English SDK that takes English instructions and compiles them into PySpark objects like DataFrame.

The pyspark-ai leverages langchain and openai framework to use GenAI Large Language Models (LLM) to simplify the usage of PySpark. The openai is an opensource framework that is used to interact with the OpenAI GPT models, whereas langchain is also a open-source framework that allows you to interact with several LLM models seamlessly; this abstracts the complex code to use with LLM model APIs.

By default, PySpark English SDK uses the OpenAI GPT-4 model to translate English instructions to PySpark code and provides methods to choose your own LLM model.

## Install pyspark-ai

You can use the Python pip command to install English SDK pyspark-ai from PyPI .

```

# Install pyspark-ai
pip install pyspark-ai

```

Since pyspark-ai uses openai and langchain underlying, use the below commands to install these packages. Make sure you check the pyspark-ai documentation to find the right version to use for these. The following commands install the latest version.

```

# Install openai
pip install openai

# Install langchain
pip install langchain

```

## Create OpenAI LLM Keys

In order to use English SDK, you need a GenAI LLM model. As of writing this article, OpenAI’s LLM model named GPT-4 works with the English SDK by default; hence, I will use the OpenAI GPT-4 model in this article to use the English language and explain how to use other models.

To use the GPT-4 model, first, you need to create an account at openai.com and have your API key generated.

Create API Key

From openai.com, navigate to the API Keys section from the left menu to generate API keys.

pyspark english sdk

Use the API-keys link from OpenAI to create a new API secret key, as shown below. Remember to save this secret key somewhere safe; In case you lose it, you’ll need to generate a new one.

By pressing the Create secret key , it generates the secret key.

Set the API Key to the Environment variable

Now, copy the key and set it to the environment variable OPENAI_API_KEY .

```

# Set key to environment variable
export OPENAI_API_KEY='<paste api key>'

```

For testing purposes, I am setting the environment variable in the Python program, as shown below. For real-time applications, you should not set the key in the Python code for security purposes. Instead, you should use environment variables or other approaches that allow the safe use of your key.

```

# Set Key to environment variable in Python
import os
os.environ["OPENAI_API_KEY"]="paste api key"

```

## Using PySpark AI with Example

In this section, I will demonstrate how to initialize and activate AI capabilities in PySpark, Create DataFrame, and use natural English language to perform transformations on DataFrame.

### Initialize SparkAI

To use AI with PySpark, first, you need to Initialize the Spark AI instance. SparkAI is a Python class that creates a SparkSession object, and it contains the AI utility methods.

```

# Import PySpark AI
from pyspark_ai import SparkAI

# Create SparkAI
spark_ai = SparkAI(verbose=True)

```

I am using verbose=True to get details on the console to understand how AI is processing our query and getting us the result.

SparkAI also provides a parameter to supply the SparkSession object if you already have one. This input spark session object is assigned to _spark variable within the SparkAI class. So to access the spark session, ideally, you should use spark_ai._spark .

```

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.getOrCreate()

# Create SparkAI by using existing SparkSession object
spark_ai = SparkAI(spark_session=spark, verbose=True)

```

### Activate AI Capabilities

To activate AI capabilities in Spark DataFrame, you have to activate it using the activate() method. This enables the DataFrame to use natural language to perform transformations.

```

# Activate
spark_ai.activate()

```

### Create DataFrame

Let’s create a sample DataFrmae with column names firstname , lastname , country , state and salary .

```

# Create DataFrame in PySpark
data = [("James","Smith","USA","CA",200000),
    ("Michael","Rose","USA","NY",150000),
    ("Robert","Williams","USA","CA",120000),
    ("Maria","Jones","USA","NY",130000),
    ("Ramana","Madala","India","AP",40000),
    ("Chandra","Potte","India","AP",50000),
    ("Krishna","Murugan","India","TN",40000),
    ("Saravanan","Murugan","India","TN",40000),
  ]
columns = ["firstname","lastname","country","state","salary"]
df = spark_ai._spark.createDataFrame(data, schema=columns)
df.show()

# Output:
#+---------+--------+-------+-----+------+
#|firstname|lastname|country|state|salary|
#+---------+--------+-------+-----+------+
#|    James|   Smith|    USA|   CA|200000|
#|  Michael|    Rose|    USA|   NY|150000|
#|   Robert|Williams|    USA|   CA|120000|
#|    Maria|   Jones|    USA|   NY|130000|
#|   Ramana|  Madala|  India|   AP| 40000|
#|  Chandra|   Potte|  India|   AP| 50000|
#|  Krishna| Murugan|  India|   TN| 40000|
#|Saravanan| Murugan|  India|   TN| 40000|
#+---------+--------+-------+-----+------+

```

Here, _spark is a SparkSession object, and createDataFrame() from SparkSession is used to create a DataFrame.

Alternatively, you can create a DataFrame by querying an LLM from the web search result.

```

# Create DataFrame from web
auto_df = spark_ai.create_df("https://www.structnet.com/instructions/zip_min_max_by_state.html")
auto_df.show()

```

This reads the data from the specified URL, creates a temporary view, and selects the data from the view to create a Dataframe. To perform this task, it uses the GenAI capabilities.

### Rename Column Names using English Instruction

By using the natural language instruction, change the column names of the DataFrame.

```

# Rename columns using AI
df2 = df.ai.transform("rename column name from firstname to first_name and lastname to last_name")
df2.printSchema()
df2.show()

```

Yields below output. Note that column names firstname and lastname have been changed to first_name and last_name , respectively.

From df.ai , ai is an object of AIUtils class, which provides the transform() and other AI utility methods that I will use in the next sections.

If you notice the above output, English SDK first creates the temporary view from the DataFrame, translates the natural language to SQL query using a specified LLM model, and executes the SQL query to get the desired result.

### Apply Transformation using English Instruction

Now, let’s apply the transformation by providing instructions in the natural English language. We can use the ai.transform() function with the instructions.

```

# Apply transformation using english language
df3 = df2.ai.transform("calculate total salary for each state and country")
df3.show()

```

Yields below output.

## Plot the Result using AI

Let’s plot the result of the DataFrame using AI. To use the plot, you need to install the plotly package.

```

# Plot DataFrame using AI
df3.ai.plot()

```

This displays the DataFrame contents as a bar chart.

pyspark plot natural language

If you had to write this in coding, you should write something like below. This code first converts the PySpark DataFrame to a Pandas DataFrame using the `toPandas()` method. Then, it creates a bar chart using Plotly’s `go.Bar` function, with `state` as the x-axis and `sum` as the y-axis.

```

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

```

In case you want the result in a pie chart, you can easily achieve this by specifying it in English as an argument to plot() method.

```

# Plot DataFrame using AI
df3.ai.plot("display in pie chart")

```

This displays the result in the pie chart.

pyspark pie chart

## Explain DataFrame using AI

The explain() provides the explanation of DataFrame operations in natural language that can easily be understood.

```

# Explain DataFrame
df3.ai.explain()

```

Yields below output

## Verify the Result

You can use the ai.verify() function to verify the results by checking some criteria. This method is very helpful and handy for running test cases for the provided PySpark dataframe transformation function.

This returns True if the transformation is valid; otherwise, False .

```

# Verify
df3.ai.verify("should have 4 stats")

```

Yields below output

pyspark ai english sdk

## Commit

Use the spark_ai.commit() to persist the result permanently. This basically commits the staging in-memory cache into the persistent cache, if the cache is enabled.

```

# Commit
spark_ai.commit()

```

## Choosing Other GPT LLM Model

PySpark AI provides the flexibility to work with several other LLM models.

Using GPT3.5-turbo Model

The snippet below is an example of how to instantiate SparkAI with a GPT3.5-turbo model. Note that this produces lower output quality; hence, you may see incorrect results.

```

# Using other LLM model
from langchain.chat_models import ChatOpenAI
from pyspark_ai import SparkAI

# Use 'gpt-3.5-turbo' (might lower output quality)
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

spark_ai = SparkAI(llm=llm, verbose=True)

```

Using Azure OpenAI Models

If you are working with Azure, you need to use the AzureChatOpenAI and specify the LLM model using the deployment_name and model_name .

```

from langchain.chat_models import AzureChatOpenAI
from pyspark_ai import SparkAI

llm = AzureChatOpenAI(
    deployment_name=...,
    model_name=...
)
spark_ai = SparkAI(llm=llm)
spark_ai.activate()

```

## Conclusion

By utilizing English instructions, users can obtain analytical results without needing to learn the DataFrame API or SQL. This simplifies the process and reduces the learning curve associated with PySpark. By default, PySpark English SDK uses the OpenAI GPT-4 model to translate English instructions into PySpark code. However, users have the flexibility to select their preferred LLM model. This approach significantly reduces the complexity of coding with PySpark, enabling users to interact with data using natural language instructions.

