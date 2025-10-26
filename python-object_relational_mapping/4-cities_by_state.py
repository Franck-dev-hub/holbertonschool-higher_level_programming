#!/usr/bin/python3
"""
List all cities with linked state from the db
"""
import sys
import MySQLdb


def main():
    """
    main - Main function
    Return: Void
    """
    if len(sys.argv) != 4:
        print("Usage: {} <user> <passwd> <db>".format(sys.argv[0]))
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
            sql = """
                SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states
                ON states.id = cities.state_id
                ORDER BY cities.id ASC
                """
            cur.execute(sql)

            for row in cur.fetchall():
                print(row)

    except MySQLdb.Error as e:
        print("MySQL error: {}".format(e))

    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()
