#!/usr/bin/python3
import sys
import re
import signal

# Initialize variables to store file size and status code counts
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Function to handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    """Signal handler function to print statistics on keyboard interruption."""
    print_stats()
    sys.exit(0)

# Function to print statistics
def print_stats():
    """Function to print accumulated file size and status code counts."""
    global total_file_size, status_code_counts
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(status_code, ":", status_code_counts[status_code])

# Register signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Regular expression pattern to match the input format
pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$')

# Main loop to read from standard input line by line
try:
    for i, line in enumerate(sys.stdin, start=1):
        # Check if line matches the expected format
        match = re.match(pattern, line.strip())
        if match:
            # Extract file size and status code from the matched groups
            file_size = int(match.group(4))
            status_code = int(match.group(3))

            # Accumulate file sizes
            total_file_size += file_size

            # Increment status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            # Print statistics after every 10 lines
            if i % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_stats()