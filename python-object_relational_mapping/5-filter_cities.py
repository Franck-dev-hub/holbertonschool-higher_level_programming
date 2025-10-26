#!/usr/bin/python3
"""
List specific states
"""
import sys
import MySQLdb


def main():
    """
    main - Main function
    Return: Void
    """
    if len(sys.argv) != 5:
        print("Usage: {} <user> <passwd> <db> <statename>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
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
                SELECT cities.name FROM cities
                INNER JOIN states
                ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """
            cur.execute(sql, (state_name,))
            rows = cur.fetchall()

            if rows:
                print(", ".join(row[0] for row in rows))
            else:
                print()

    except MySQLdb.Error as e:
        print("MySQL error: {}".format(e))

    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()
