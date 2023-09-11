# AI School Data Engineering Project

> ## Disclaimer: Code Access Restriction
>
>Dear Participant,
>
>As part of this challenge, it is imperative that you approach the provided data with integrity and adhere to the guidelines set forth in this document. To ensure a fair and educational experience, we have intentionally restricted access to the code responsible for generating the data used in this project.
>
>Please refrain from attempting to access, reverse engineer, or use the code that generates the data. Doing so undermines the purpose of this challenge and may result in disqualification from the project.
>
>The intention behind this restriction is to encourage you to focus on the data engineering aspects, such as extraction, transformation, and loading processes, rather than on the data generation itself.
>
>We trust that you will respect this requirement and engage with the challenge in a spirit of honesty and learning.
>
>Thank you for your understanding and cooperation.


# Business case

## Introduction

In the era of data-driven decision-making, organizations are increasingly relying on data to gain insights, optimize operations, and make informed choices. Our fictional company, HR Insights, is no exception. As a leading Human Resources (HR) company, HR Insights specializes in gathering, managing, and analyzing extensive volumes of personnel data from various sources.

## The Challenge

HR Insights operates in a data-rich environment where information about employees, job applicants, and HR processes is continuously generated. This data is often unstructured, coming from sources like job applications, payroll records, employee surveys, and more. The challenge lies in efficiently collecting, processing, and storing this data for meaningful analysis and strategic decision-making.

## Data Integration

Our HR company faces the complex task of integrating data from diverse sources into a unified system. This integration process involves combining data about employees' personal information, job history, performance metrics, and even financial data like bank information and tax records. To make this data useful for HR professionals and decision-makers, it must be organized, cleaned, and structured.

## Data Lakes and Data Warehouses

To address this challenge, HR Insights is exploring the implementation of modern data architecture concepts, including Data Lakes and Data Warehouses.

### Data Lakes

A Data Lake is a centralized repository that allows HR Insights to store vast amounts of raw data in its native format. Data Lakes provide flexibility in handling both structured and unstructured data, making them ideal for capturing the diverse data sources we encounter. With Data Lakes, we can accumulate data quickly and without the need for extensive preprocessing.

### Data Warehouses

On the other hand, a Data Warehouse is designed for structured, organized, and optimized data storage. It serves as a highly structured repository for curated data that is ready for analysis and reporting. Data Warehouses help HR Insights consolidate data from various sources, transforming it into a format that is easy to query and analyze.

## Project Goal

The goal of this pedagogical project is to provide you, the students, with hands-on experience in solving real-world data engineering challenges. You will be tasked with implementing an Extract, Transform, Load (ETL) process to collect, process, and store HR data from Kafka, an event streaming platform, into both a MongoDB and a SQL Database. This project will not only test your technical skills but also your ability to make informed decisions regarding data organization and architecture.


# Installation guide

1. Make sure Docker is installed in your machine
2. Make sure docker-compose is also installed
3. Execute the following command:

``docker-compose up --build``

For next executions, you can omit the "--build" flag. If you wish to launch the generator in detached mode, use "-d" flag.

# Data structure

The JSON data you'll interact with may encompass various types of information. This could range from personal details, such as names and addresses, to more transactional data like financial records. The diversity in data types is intended to provide a comprehensive and representative dataset that mirrors the complexities faced by organizations in managing information.

Embracing this variability and diversity in the data is a fundamental aspect of this challenge. It will require you to implement robust ETL processes capable of handling a wide range of data points and ensuring accurate storage and retrieval.

The goal of this project is to equip you with practical experience in data engineering, where adaptability and versatility are key skills. Embrace the diversity of the data and leverage it as an opportunity to refine your data processing techniques.

These are the schemas you will find:

- Personal data:
  - Name
  - Lastname
  - Sex
  - Telfnumber
  - Passport
  - E-Mail  

- Location:
  - Fullname
  - City
  - Address

- Professional data:
  - Fullname
  - Company
  - Company Adress
  - Company Telfnumber
  - Company E-Mail
  - Job

- Bank Data 
  - Passport
  - IBAN
  - Salary

- Net Data
  - Address
  - IPv4

Remember that you will have to join the data from the same person to store them together. Check the data carefully, as they may not be consistent.