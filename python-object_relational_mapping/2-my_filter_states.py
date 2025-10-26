#!/usr/bin/python3
"""
List all states with names match the argument
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
            cur.execute("""
                        SELECT * FROM states
                        WHERE name = BINARY '{}'
                        ORDER BY id ASC
                        """
                        ).format(state_name)

            for row in cur.fetchall():
                print(row)

    except MySQLdb.Error as e:
        print("MySQL error: {}".format(e))

    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()
