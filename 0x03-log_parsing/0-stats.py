#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics
"""

import sys

def print_stats(total_size, status_counts):
    """
    Print the accumulated metrics.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 10:
            continue
        ip, _, _, datetime, _, method, url, protocol, status_code, file_size = parts
        if method != '"GET':
            continue
        try:
            status_code = int(status_code)
            file_size = int(file_size)
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            continue
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)
except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_counts)
