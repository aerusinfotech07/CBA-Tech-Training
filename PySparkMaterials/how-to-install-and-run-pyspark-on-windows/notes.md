# How to Install PySpark on Windows

---

In this article, we’ll focus specifically on how to install PySpark on the Windows operating system. While Spark is primarily designed for Unix-based systems, setting it up on Windows can sometimes be a bit tricky due to differences in environment and dependencies. However, with the right steps and understanding, you can install PySpark into your Windows environment and run some examples.

Advertisements

I will also cover how to start a history server and monitor your jobs using Web UI .

Related:
- PySpark Install on Mac OS
- Install Apache Spark on Windows (Spark with Scala)

To Install PySpark on Windows follow the below step-by-step instructions.

## Install Python or Anaconda distribution

Download and install either Python from Python.org or Anaconda distribution which includes Python, Spyder IDE, and Jupyter Notebook. I would recommend using Anaconda as it’s popular and used by the Machine Learning and Data science community.

To use Anaconda distribution, follow Install PySpark using Anaconda & run Jupyter notebook

## Install Java 8

To run the PySpark application, you would need Java 8/11/17 or a later version. Download and install JDK from OpenJDK .

Once the installation completes, set JAVA_HOME and PATH variables as shown below. Change the JDK path according to your installation.

```

JAVA_HOME = C:\Program Files\Java\jdk1.8.0_201
PATH = %PATH%;C:\Program Files\Java\jdk1.8.0_201\bin

```

## PySparkInstall on Windows

You can install PySpark either by downloading binaries from spark.apache.org or by using the Python pip command.

### Install using Python PiP

Python pip, short for “Python Package Installer,” is a command-line tool used to install, manage, and uninstall Python packages from the Python Package Index (PyPI) or other package indexes. PyPI is a repository of software packages developed and shared by the Python community.

PySpark is available in PyPI hence, you can install it using the pip command.

```

# Install pyspark using pip command
pip install pyspark

```

### Download & Install from spark.apache.org

If you install PySpark using PIP, then skip this section.

Access the Spark Download page, choose the Spark release version and package type; the link on point 3 updates to the selected options. select the link to download it.
Screenshot
2. Unzip the binary using WinZip or 7zip and copy the underlying folder spark-3.5.1-bin-hadoop3 to c:\apps

3. Open the Windows environment setup screen and set the following environment variables.

```

SPARK_HOME  = C:\apps\spark-3.5.1-bin-hadoop3
HADOOP_HOME = C:\apps\spark-3.5.1-bin-hadoop3
PATH=%PATH%;C:\apps\spark-3.5.1-bin-hadoop3\bin

```

Install winutils.exe on Windows

<br> winutils.exe is a set of utilities for Windows used in Hadoop deployments. These utilities are primarily required for running Apache Hadoop applications on a Windows operating system. Copy winutils files to %SPARK_HOME%\bin folder.

## PySpark shell

The PySpark shell is an interactive Python shell that provides a convenient way to interact with Apache Spark. To launch the PySpark shell, you typically use the pyspark command in your terminal or command prompt. Once launched, you’ll see the Python interpreter prompt ( >>> ) indicating that you can start executing Python code. From there, you can import the pyspark module and start interacting with Spark.

pyspark shell windows
Screenshot
Run the below statements in PySpark shell to create an RDD.

```

# RDD creation
rdd = spark.sparkContext.parallelize([1,2,3,4,5,6])
print(rdd.count)

```

Spark-shell generates a Spark context web UI, which is accessible by default at http://localhost:4040 .

## Web UI

The Spark Web UI or Spark UI, is a web-based interface provided by Apache Spark for monitoring and managing Spark applications. It offers real-time insights into the execution of Spark jobs, providing information about tasks, stages, executors, and more.

You can access Spark Web UI by accessing http://localhost:4040. You can find this URL on the PySpark shell console.

## Conclusion

In summary, you have learned how to install PySpark on Windows and run sample statements in spark-shell. If you have any issues setting it up, please message me in the comments section, and I will try to respond with a solution.

Happy Learning !!

## Related Articles
- Apache Spark Setup with Scala and IntelliJ
- Apache Spark Installation on Windows
- Spark Installation on Linux Ubuntu
- Spark Hello World Example in IntelliJ IDEA
- Spark Word Count Explained with Example
- Spark Setup on Hadoop Cluster with Yarn
- Spark Start History Server
- How to Check Spark Version
- Install PySpark on Ubuntu running on Linux
- Install PySpark in Anaconda & Jupyter Notebook
- Install PySpark in Jupyter on Mac using Homebrew
- How to Install PySpark on Mac
- Install Pyspark using pip or condo
- Dynamic way of doing ETL through Pyspark How to Find PySpark Version? PySpark Shell Command Usage with Examples Install Anaconda & Run pandas on Jupyter Notebook
- Pyspark: Exception: Java gateway process exited before sending the driver its port number

