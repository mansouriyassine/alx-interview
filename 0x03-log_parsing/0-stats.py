#!/usr/bin/python3
import sys
import re
import signal

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def signal_handler(sig, frame):
    """
    Signal handler function for SIGINT signal (Ctrl+C).
    Prints statistics and exits gracefully upon receiving the signal.
    
    Parameters:
        sig (int): The signal number.
        frame (frame): The current stack frame.
    """
    print_stats()
    sys.exit(0)

def print_stats():
    """
    Prints accumulated file size and status code counts.
    """
    global total_file_size, status_code_counts
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(status_code, ":", status_code_counts[status_code])

signal.signal(signal.SIGINT, signal_handler)

pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 '
                     r'HTTP/1.1" (\d+) (\d+)$')

try:
    for i, line in enumerate(sys.stdin, start=1):
        match = re.match(pattern, line.strip())
        if match:
            file_size = int(match.group(4))
            status_code = int(match.group(3))
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            if i % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()