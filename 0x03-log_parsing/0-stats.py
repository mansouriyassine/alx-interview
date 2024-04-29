#!/usr/bin/python3
import sys
import signal

status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0
line_count = 0


def print_stats():
    """Prints the current statistics."""
    print("File size:", total_file_size)
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def signal_handler(sig, frame):
    """Handler for the SIGINT signal (CTRL+C)."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) == 7:
        ip_address, _, _, _, status_code, file_size = parts
        try:
            status_code = int(status_code)
            file_size = int(file_size)
            if status_code in status_counts:
                status_counts[status_code] += 1
                total_file_size += file_size
                line_count += 1
                if line_count % 10 == 0:
                    print_stats()
        except ValueError:
            continue

print_stats()