import sqlite3

"""
__enter__ and __exit__ is parts of the context manager protocol in Python, allowing the use of the with statement.
When you use with, Python automatically calls __enter__() at the start of the block and __exit__() at the end.
"""

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = ("INSERT INTO books VALUES "
                                   "('If Tomorrow Comes', 'Sidney Sheldon'), "
                                   "('The Lincoln Lawyer', 'Michael Connelly')")
select_from_table_sql_statement = 'SELECT * FROM books'


# Context manager
class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type: holds the type of the exception
        # exc_val: holds the value of the exception
        # exc_tb: holds the traceback

        if exc_type is not None:
            print(f'an error occurred: {exc_val}')

        self.connection.close()


def main():
    with Database(':memory:') as db:
        db.cursor.execute(create_table_sql_statement)
        db.connection.commit()

        db.cursor.execute(insert_into_table_sql_statement)
        db.connection.commit()

        db.cursor.execute(select_from_table_sql_statement)
        data = db.cursor.fetchall()
        print(data)


if __name__ == "__main__":
    main()
