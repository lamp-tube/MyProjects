Learning Pyspark from freecodecamp (https://www.youtube.com/watch?v=_C8kWso4ne4)

Apache Spark is a fast and general-purpose cluster computing system.

run below commands in pycharm notbook- (install pycharm if not installed)

-> !pip install pyspark

create a small dataset test1.csv

-> import pandas as pd
->pd.read.csv('test1.csv')

-> from pyspark.sql import SparkSession
-> spark=SparkSession.builder.appName('session-name').getOrCreate()
-> spark

->df_spark=spark.read.csv('test1.csv')
->df_spark
->df-spark.show()

->spark.read.option('header','true').csv('test1.csv').show()

->type(df_spark) => pyspark.sql.classic.dataframe.dataframe

->df_spark.head(3)
->df_spark.printscheme()

## next topics
1. Pypspark dataframe
2. Reading the dataset
3. Checking the Datatypes of the column(schema)
4.selecting columns and indexing
5.check describe option similar to pandas
6. adding columns / dropping columns