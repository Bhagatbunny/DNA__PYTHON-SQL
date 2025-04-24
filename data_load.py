import pandas as pd
import os
from dotenv import load_dotenv
from transformations import CustomerTransformer, ProductTransformer, OrderTransformer
from utils import FileUtils
from connect_to_pgsql import get_db_connection
from sqlalchemy import text
# from extract_files import download_kaggle_dataset


load_dotenv()

logger = FileUtils.set_logger("data_load")
engine = get_db_connection()
file_path = os.getenv('LOCAL_PATH')

def load_csv(file_name):
    """Loads a CSV file."""
    try:
        logger.info(f"Loading file: {file_name}")
        return pd.read_csv(os.path.join(file_path, file_name))
    except Exception as ex:
        logger.error(f"Error loading file {file_name}: {ex}")
        raise

def save_csv(df, file_name):
    """Saves a DataFrame to a CSV file."""
    try:
        output_path = os.path.join(file_path, file_name)
        df.to_csv(output_path, index=False)
        logger.info(f"File saved: {output_path}")
    except Exception as ex:
        logger.error(f"Error saving file {file_name}: {ex}")
        raise

def load_to_postgres(df, table_name, connection):
    """Truncate the table and save the DataFrame to PostgreSQL."""
    try:
        if not df.empty:
            schema = os.getenv("SCHEMA")
            logger.info(f"Truncating and loading data to: {schema}.{table_name}")
            
            truncate_sql = text(f'TRUNCATE TABLE "{schema}"."{table_name}" RESTART IDENTITY CASCADE;')
            connection.execute(truncate_sql)
            logger.info(f"Truncated table: {schema}.{table_name}")

            df.to_sql(table_name, connection, if_exists="append", index=False, schema=schema)
            # logger.info(f"Inserted data into {schema}.{table_name}")
            logger.info(f"Inserted {len(df)} rows into {schema}.{table_name}")
            FileUtils.verify_row_count(connection, schema, table_name, len(df), logger)
        else:
            logger.warning("No data to insert.")
    except Exception as e:
        logger.error(f"Error inserting into PostgreSQL: {e}")


def process_and_save_data(file_names, transformers, output_files, connection):
    """Process and save transformed data."""
    for table_name, transformer in transformers.items():
        df = load_csv(file_names[table_name])
        logger.info(f"{table_name}: Raw data row count = {len(df)}")
        transformed_df = transformer(df)
        save_csv(transformed_df, output_files[table_name])
        load_to_postgres(transformed_df, table_name, connection)

def main():
    # Define file names and transformers
    logger.info("------------ starting data load process ------------")
    
    file_names = {
        'customers': 'customers.csv',
        'products': 'products.csv',
        'orders': 'orders.csv'
    }
    output_files = {
        'customers': 'customers_transformed.csv',
        'products': 'products_transformed.csv',
        'orders': 'orders_transformed.csv'
    }
    transformers = {
        'customers': CustomerTransformer.transform,
        'products': ProductTransformer.transform_products,
        'orders': OrderTransformer.transform_orders
    }

    # Ensure output directory exists
    FileUtils.check_and_create(file_path, logger)

    # Process and save data
    # process_and_save_data(file_names, transformers, output_files)
    logger.info("Creating Database connection...")
    with engine.begin() as connection:
        logger.info("Database connection successful.")
        process_and_save_data(file_names, transformers, output_files, connection)
    logger.info("------------ data load process completed ------------")

if __name__ == "__main__":
    main()
