# ETL Data Load Pipeline – PostgreSQL Integration

A Python-based ETL (Extract, Transform, Load) pipeline that automates the transformation and loading of structured data from CSV files into a PostgreSQL database. This project is modular, efficient, and designed for scalability and reusability.

---

## Project Overview

This project addresses the need for a reliable data ingestion pipeline by providing:

- Automated data extraction from CSV files  
- Structured transformations through custom Python classes  
- Seamless loading into PostgreSQL with data integrity checks  
- Detailed logging for traceability and debugging

---

## What I Did

- Implemented environment variable management using `dotenv` for secure and flexible configuration  
- Developed transformation logic for `customers`, `products`, and `orders` datasets  
- Built a logging system to monitor each step of the ETL process  
- Created a PostgreSQL integration using SQLAlchemy, with schema-level control  
- Ensured data quality by truncating target tables and validating row counts  
- Designed the pipeline to be modular and easy to extend for other datasets

---

## Tech Stack

- Python  
- Pandas for data manipulation  
- SQLAlchemy for PostgreSQL connection  
- `python-dotenv` for environment variable management  
- Custom transformation classes for data cleaning and restructuring  
- PostgreSQL as the destination database

---

## Key Features

- Modular and reusable transformation architecture  
- Automatic directory checks and CSV file validation  
- Truncates tables before inserting data to avoid duplicates  
- Validates row count post-insertion for data accuracy  
- Comprehensive logging for easy monitoring and debugging

---

## Contributing

This project can be extended by adding new transformers or integrating additional data sources.  
Feel free to fork the repository and customize it to suit your use case.
