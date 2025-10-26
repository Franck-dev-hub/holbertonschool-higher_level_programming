#!/usr/bin/python
"""
List all states from the database
"""
import sys
import MySQLdb


def main():
    """
    main - Main function
    Return: Void
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    db = None

    try:
        # Connecting to a MySQL database
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database,
                charset="utf8"
                )

        # Getting a Cursor in MySQL Python
        with db.cursor() as cur:
            # Executing MySQL Queries in Python
            cur.execute("""SELECT * FROM states
                        ORDER BY id ASC""")

            # Obtaining Query Results
            for row in cur.fetchall():
                print(row)

    except MySQLdb.Error as e:
        print("MySQL error: {}".format(e))

    finally:
        # Clean up
        if db:
            db.close()


if __name__ == "__main__":
    main()
