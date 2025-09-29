#!/usr/bin/python3

"""
101-stats.py
Read stdin
"""

import sys

def print_stats(total_size, status_count):
    """
    print_stats - Print accumulated stats
    @total_size: Total size cumulated
    @status_count: Status counter
    Return: Void
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_count.keys()):
        print("{}: {}".format(code, status_count[code]))

def main():
    """
    main - Main function
    Return: Void
    """
    total_size = 0
    status_count = {}
    line_count = 0
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) < 7:
                continue

            try:
                size = int(parts[-1])
                total_size += size
            except ValueError:
                pass

            try:
                status = int(parts[-2])
                if status in valid_codes:
                    status_count[status] = status_count.get(status, 0) + 1
            except ValueError:
                pass

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_count)

    except KeyboardInterrupt:
        print_stats(total_size, status_count)
        raise

if __name__ == "__main__":
    main()
