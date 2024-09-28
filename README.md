# Paris Olympics 2024 Data Engineering Project

The Paris Olympic Data Analysis on Azure project is a comprehensive solution for analyzing and visualizing Olympic Games data using various Azure services. This project aims to showcase how to leverage the power of cloud computing and Azure's data services to gain insights from Olympic data. By combining Azure Databricks, Azure Data Factory, and other Azure resources, this project provides a scalable and efficient way to process, transform, and analyze large volumes of Olympic data.

## Introduction:
The Olympic Data Analysis on Azure project demonstrates how to build an end-to-end data analysis pipeline on the Azure cloud platform. This involves ingesting raw Olympic data, transforming it into a suitable format, performing analysis, and creating insightful visualizations. The project provides an example of how to integrate and utilize Azure Databricks, Azure Data Factory, Azure Synapse, Azure Key Vault and Azure Data Lake Gen 2 to achieve these goals.

## Architecture:

![image](https://github.com/user-attachments/assets/6e8ba6d5-8f6f-4601-92af-377e15ebceb3)

The architecture of the project consists of the following components:
-	On-Prem SQL Database: Stores the cleaned and transformed data, making it accessible for visualization and reporting.
-	Azure Data Factory: Manages and orchestrates the data workflow. It is responsible for data ingestion from various sources, data transformation, and scheduling of jobs.
-	Azure Storage: Serves as the data lake for storing raw and processed data. It can also host intermediate results generated during the analysis.
-	Azure Data Vault: Used to store and access secrets, such as API keys, passwords, certificates, and cryptographic keys.
-	Azure Databricks: Used for data processing, transformation, and analysis. It provides a collaborative and interactive environment for running Spark-based jobs.
-	Power BI: Connects to the Azure SQL Database to create interactive and visually appealing dashboards for data exploration.

## Technologies Used
- Azure Databricks
-	Azure Data Factory
- Azure Storage
-	SQL Database
-	Azure Synapse Analytics
-	Azure Key Vault

![image](https://github.com/user-attachments/assets/4970283d-824c-4355-b96c-89abfa1c4b8b)

## Current Environment
-	Utilized the Paris Olympics dataset from Kaggle.
-	Set up an on-premises Microsoft SQL server on a personal computer.
-	Imported the dataset using Microsoft SQL Server Management Studio.
-	Created a new user profile, "sqluser."
-	Saved "sqluser" profile's password credentials as a Secret in Azure Key Vault.

![image](https://github.com/user-attachments/assets/fe374c78-33b3-4b4a-a400-4c37a7a59790)

## 1: Data Ingestion
Data ingestion from the on-premises SQL server to Data Lake Gen 2 is accomplished via Azure Data Factory. The process involves:
1.	Installation of Self-Hosted Integration Runtime.
2.	Establishing a connection between Azure Data Factory and the local SQL Server.
3.	Setting up a copy pipeline to transfer all tables from the local SQL server to the Azure Data Lake's "bronze" folder.


 ![image](https://github.com/user-attachments/assets/28fc4fba-8b96-4ffb-a6a5-2bb4e705a34a)

## 2: Data Transformation
After ingesting data into the "bronze" folder, it is transformed following the medallion data lake architecture (bronze, silver, gold). Data transitions through bronze, silver, and ultimately gold, suitable for business reporting tools like Power BI.
Azure Databricks, using PySpark, is used for these transformations. Data initially stored in parquet format in the "bronze" folder is converted to the delta format as it progresses to "silver" and "gold." This transformation is carried out through Databricks notebooks:
1.	Mount the storage.
2.	Transform data from "bronze" to "silver" layer.
3.	Further transform data from "silver" to "gold" layer.


Azure Data Factory is updated to execute the "bronze" to "silver" and "silver" to "gold" notebooks automatically with each pipeline run.

![image](https://github.com/user-attachments/assets/ddba0249-5939-4a39-9586-780a64a12a0c)

## 3: Data Loading:
Data from the "gold" folder is loaded into the Business Intelligence reporting application, Power BI. Azure Synapse is used for this purpose. The steps involve:
1.	Creating a link from Azure Storage (Gold Folder) to Azure Synapse.
2.	Writing stored procedures to extract table information as a SQL view.
3.	Storing views within a server-less SQL Database in Synapse.

![image](https://github.com/user-attachments/assets/aca32e33-9eef-48c6-a5ab-29650b653cb4)

## 4: Data Reporting
Power BI connects directly to the cloud pipeline using DirectQuery to dynamically update the database. A Power BI report is developed to visualize Olympics dataset data, including Athletes, Medals, and Country.



https://github.com/user-attachments/assets/5898f8e3-649d-4658-bec9-580ccb3a7f4e



## 5: Conclusion
The Olympic Data Analysis on Azure project demonstrates how to leverage Azure services for processing, analyzing, and visualizing large-scale data.

