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

