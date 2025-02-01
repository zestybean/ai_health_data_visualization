import sqlite3
import csv
import os
import pandas as pd

# Set the database path to the root of the project
DB_PATH = "Assignment_MIMIC_SQL/database.db"

def create_or_update_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Directory containing CSV files
        data_dir = "Assignment_MIMIC_SQL/data/mimic_data"
        
        # List all CSV files in the directory
        csv_files = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.csv')]

        for file in csv_files:
            # Read CSV file in chunks using pandas
            table_name = os.path.splitext(os.path.basename(file))[0]
            chunk_size = 10000  # Adjust the chunk size as needed

            for chunk in pd.read_csv(file, chunksize=chunk_size):
                if chunk.empty:
                    continue

                # Create table if doesn't exist and insert data
                chunk.to_sql(table_name, conn, if_exists='append', index=False)

        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def clear_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Get the list of all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Drop each table
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")
            print(f"Dropped table {table[0]}")

        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    create_or_update_database()