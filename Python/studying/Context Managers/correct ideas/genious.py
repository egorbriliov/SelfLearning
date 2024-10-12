import sqlite3
from contextlib import contextmanager

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = ("INSERT INTO books VALUES "
                                   "('If Tomorrow Comes', 'Sidney Sheldon'), "
                                   "('The Lincoln Lawyer', 'Michael Connelly')")
select_from_table_sql_statement = 'SELECT * FROM books'


@contextmanager
def database(path: str):
    connection = sqlite3.connect(path)
    try:
        cursor = connection.cursor()
        yield {'connection': connection, 'cursor': cursor}
    except Exception as e:
        print(f'an error occurred: {e}')
    finally:
        connection.close()


def main():
    database_path = ":memory:"

    with database(database_path) as db:
        db.get('cursor').execute(create_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(insert_into_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(select_from_table_sql_statement)
        data = db.get('cursor').fetchall()

        print(data)


if __name__ == "__main__":
    main()
