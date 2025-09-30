# PySpark Shell Command Usage with Examples

---

PySpark (Spark with python) default comes with an interactive pyspark shell command (with several options) that is used to learn, test PySpark examples and analyze data from the command line. Since Spark supports Scala, Python, R, and Java, It provides different shells for each language. But for Java, there is no shell. If you are using Scala then use spark-shell and for R language use sparkr .

Advertisements

PySpark Shell Key Points –
1. PySpark shell is referred as REPL (Read Eval Print Loop) which is used to quickly test PySpark statements.
1. Spark shell is available for Scala, Python and R (Java might be supported in previous versions).
1. The pyspark command is used to launch Spark with Python shell also call PySpark.
1. Use spark-shell command to work Spark with Scala .
1. The sparkr command is used to launch Spark with R language.
1. PySpark shell default provides spark and sc variables. spark is an object of SparkSession and sc is an object of SparkContext .
1. In PySpark shell, you cannot create your own SparkContext.

Pre-requisites: Before you proceed make sure you have PySpark installed.
- Install PySpark on Mac OS
- Install PySpark on Windows
- Install PySpark in Anaconda

## 1. Launch PySpark Shell Command

Go to the Spark Installation directory from the command line and type bin/pyspark and press enter, this launches pyspark shell and gives you a prompt to interact with Spark in Python language. If you have set the Spark in a PATH then just enter pyspark in command line or terminal (mac users).

```

./bin/pyspark

```

Yields below output. It also supports several command-line options which I will cover in the below sections.

pyspark shell command

To exit from the pyspark shell use quit() , exit() or Ctrl-D (i.e. EOF). Let’s understand a few statements from the above screenshot.
1. By default, pyspark creates a Spark context which internally creates a Web UI with URL localhost:4040. Since it is unable to bind on 4040 for me it was created on 4042 port.
1. Spark context created with app id local-*
1. By default it uses local[*] as master
1. Spark context and session are created with variables 'sc' and 'spark' respectively.
1. Displays Spark, and Python versions.

## 2. PySpark Shell Web UI

By default, PySpark launches Web UI on port 4040, if it could not bind then it tries on 4041, 4042, and so on until it binds. In my case, it is bound on 4046 port.

pyspark shell Web UI

## 3. Run PySpark Statements from Shell

Let’s create a PySpark DataFrame with some sample data to validate the installation, enter the following commands in the shell in the same order.

```

>>> data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
>>> df = spark.createDataFrame(data)
>>> df.show()

```

Yields below output. For more examples on Spark with python refer to PySpark Tutorial with Examples .

pyspark shell example

Use quit() , exit() or Ctrl-D (i.e. EOF) to exit from the pyspark shell.

## 4. PySpark Shell Command Examples

Let’s see the different pyspark shell commands with different options.

Example 1:

```

./bin/pyspark \
   --master yarn \
   --deploy-mode cluster

```

This launches the Spark driver program in cluster . By default, it uses client mode which launches the driver on the same machine where you are running shell.

Example 2: Below example uses other python files as dependencies.

```

./bin/spyspark \
   --master yarn \
   --deploy-mode cluster \
   --py-files file1.py,file2.py,file3.zip

```

Example 3: Below example uses the pyspark shell with configs.

```

./bin/pyspark \
   --master yarn \
   --deploy-mode cluster \
   --driver-memory 8g \
   --executor-memory 16g \
   --executor-cores 2  \
   --conf "spark.sql.shuffle.partitions=20000" \
   --conf "spark.executor.memoryOverhead=5244" \
   --conf "spark.memory.fraction=0.8" \
   --conf "spark.memory.storageFraction=0.2" \
   --py-files file1.py,file2.py

```

## 5. PySpark Shell Command Options

Like any other shell command, PySpark shell also provides several commands and options, you can get all available options with --help . Below are some of the important options.
PySpark Shell OptionsOption Description-I <file>preload <file>, enforcing line-by-line interpretation–master MASTER_URLspark://host:port, mesos://host:port,yarn,k8s://https://host:port, or local (Default: local[*]).–deploy-mode DEPLOY_MODEWhether to launch the driver program locally (“client”) or on one of the worker machines inside the cluster (“cluster”)(Default: client).–py-files PY_FILESComma-separated list of .zip, .egg, or .py files to place.–name NAMESpecify the name of your application.–packagesComma-separated list of maven coordinates of jars to include on the driver and executor classpaths.–files FILESComma-separated list of files to be placed in the working directory of each executor.PySpark Shell Options
For the complete list of spark-shell options use the -h command.

```

.bin/pyspark --help

```

If you closely look at it most of the options are similar to spark-submit command .

## Conclusion

In this article, you have learned What is PySpark shell, how to use it with several commands, and the different command options available.

Happy Learning !!

## Related Articles
- How to Exit or Quit from Spark Shell & PySpark?
- PySpark Read and Write MySQL Database Table
- PySpark SparkContext Explained
- How to Find PySpark Version?
- How to Install PySpark on Mac (in 2022)
- PySpark createOrReplaceTempView() Explained
- PySpark Read JDBC Table to DataFrame
- What’s New in PySpark 4.0: Features, Improvements, and Enhancements

