#!/usr/bin/python3
import sys


def print_stats(total_size, status_counts):
    """Print the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

total_size = 0
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) < 7:
            continue

        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
        except ValueError:
            continue

        total_size += file_size

        if status_code in status_counts:
            status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    pass

finally:
    print_stats(total_size, status_counts)
