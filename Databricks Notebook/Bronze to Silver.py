# Databricks notebook source
dbutils.fs.ls("/mnt/bronze/dbo/")

# COMMAND ----------

dbutils.fs.ls("/mnt/silver/")

# COMMAND ----------

input_path= '/mnt/bronze/dbo/Schedules/Schedules.parquet'

# COMMAND ----------

# create DF frame and load path
df=spark.read.format('parquet').load(input_path)

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

df= df.withColumn("start_date", date_format(from_utc_timestamp(df["start_date"].cast(TimestampType()), "UTC"), "yyyy-MM-dd") )

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %sql 
# MAGIC /*magic command to convert this into sql*/
# MAGIC select 1 as column1

# COMMAND ----------

# MAGIC %md
# MAGIC ##Doing transformation for all tables##

# COMMAND ----------

table_name = [] ##created an empty array##

for i in dbutils.fs.ls('/mnt/bronze/dbo/'):
    table_name.append(i.name.split('/')[0]) ##Appending directory name to the array##

# COMMAND ----------

table_name

# COMMAND ----------

##Created for loop to read parquet file from bronze layer and perform date conversion##
## Converted parquet file into Delta file and loaded into Silver layer##

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

for i in table_name:
    path = '/mnt/bronze/dbo/' + i + '/' + i +'.parquet'
    df=spark.read.format('parquet').load(path)
    column=df.columns

    for col in column:
        if "Date" in col or "date" in col:
            df= df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), "UTC"), "yyyy-MM-dd") )

            output_path='/mnt/silver/dbo/'+i+'/'

            df.write.format('delta').mode('overwrite').save(output_path)

# COMMAND ----------

display(df)

# COMMAND ----------

for i in table_name:
    source_path = '/mnt/bronze/dbo/'+i+'/'+i+'.parquet'
    destination_path = '/mnt/silver/dbo/'+i +'/'

    # Create the destination directory if it does not exist
    dbutils.fs.mkdirs(destination_path)

# Check if the destination directory exists and if the file is not present
    try:
        files_at_destination = [file.name for file in dbutils.fs.ls(destination_path)]

        # Check if the file is not present at the destination
        if not files_at_destination:

            # Copy the file from source to destination
                df=spark.read.format('parquet').load(source_path)
                df.write.format('delta').mode('overwrite').save(destination_path)

                #Logs
                print("File copied successfully.")
                print(files_at_destination)
        else:
            print("File already exists at the destination.")
    except Exception as e:
        print(f"Error: {str(e)}")