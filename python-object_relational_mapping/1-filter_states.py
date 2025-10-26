#!/usr/bin/python
"""
List all states with names starting with N
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
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database,
                charset="utf8"
                )

        with db.cursor() as cur:
            cur.execute("""SELECT * FROM states
                        WHERE name LIKE BINARY 'N%'
                        ORDER BY id ASC""")

            for row in cur.fetchall():
                print(row)

    except MySQLdb.Error as e:
        print("MySQL error: {}".format(e))

    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()
