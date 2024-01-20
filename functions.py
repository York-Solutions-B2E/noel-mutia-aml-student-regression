import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import csv
import os

csv_path = "./docs/data.csv"


def load_data_to_postgres_docker(csv_path, table_name, user, password, host='mypostgres', port=5432, database_name='student_grades'):
    # Load CSV data
    data = pd.read_csv(csv_path)

    # Create engine with SQLAlchemy
    password = quote_plus(password)
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database_name}')

    # Transfer data to database
    data.to_sql(table_name, engine, index=False, if_exists='replace')

load_data_to_postgres_docker(csv_path, 'your_table_name', 'leonphoenix21', 'vtlt123@dck')


def add_new_student_and_load(student_info, csv_path, table_name, database_name, user, password, host='127.0.0.1', port=5432):
    # Add new student to CSV file
    with open(csv_path, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';')

        # Use list comprehension to format the row
        row = list(student_info.values())

        print(row)
        csv_writer.writerow(row)
    # Load updated data to PostgreSQL table
    load_data_to_postgres_docker(csv_path, table_name, database_name, user, password, host, port)


# Test Student Data
new_student_info = {
    'school': 'GP',
    'sex': 'M',
    'age': 16,
    'address': 'U',
    'famsize': 'LE3',
    'Pstatus': 'T',
    'Medu': 4,
    'Fedu': 3,
    'Mjob': 'teacher',
    'Fjob': 'services',
    'reason': 'course',
    'guardian': 'mother',
    'traveltime': 3,
    'studytime': 2,
    'failures': 0,
    'schoolsup': 'no',
    'famsup': 'yes',
    'paid': 'no',
    'activities': 'yes',
    'nursery': 'yes',
    'higher': 'yes',
    'internet': 'yes',
    'romantic': 'no',
    'famrel': 5,
    'freetime': 4,
    'goout': 3,
    'Dalc': 1,
    'Walc': 2,
    'health': 1,
    'absences': 2,
    'G1': 15,
    'G2': 14,
    'G3': 15
}

add_new_student_and_load(new_student_info, csv_path, 'student_grades_table', 'student_grades', 'leonphoenix21', 'vtlt123@dck')



def delete_last_row(csv_path):
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        rows = list(csv.reader(csvfile, delimiter=';'))

    # Check if there are any rows in the CSV
    if len(rows) > 0:
        # Remove the last row
        rows.pop()

        # Write the updated rows back to the CSV file
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';')
            csv_writer.writerows(rows)
        print("Last row deleted successfully.")
    else:
        print("No rows to delete.")

# delete_last_row(csv_path)