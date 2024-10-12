import sqlite3

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = ("INSERT INTO books VALUES "
                                   "('If Tomorrow Comes', 'Sidney Sheldon'), "
                                   "('The Lincoln Lawyer', 'Michael Connelly')")
select_from_table_sql_statement = 'SELECT * FROM books'


def main():
    database_path = ':memory:'

    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    try:
        cursor.execute(create_table_sql_statement)
        connection.commit()

        cursor.execute(insert_into_table_sql_statement)
        connection.commit()

        cursor.execute(select_from_table_sql_statement)
        data = cursor.fetchall()

        print(data)

    except Exception as e:
        print(f'read or write action to the database failed: {e}')
    finally:
        connection.close()


if __name__ == "__main__":
    main()
