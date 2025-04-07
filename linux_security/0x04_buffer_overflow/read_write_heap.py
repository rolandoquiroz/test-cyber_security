#!/usr/bin/python3
"""
Script to find and replace a string in the heap of a running process
Usage: read_write_heap.py pid search_string replace_string
"""

import sys
import os
import mmap


def print_usage_and_exit():
    """Print usage information and exit with status code 1"""
    print(f"Usage: {sys.argv[0]} pid search_string replace_string")
    sys.exit(1)


def parse_maps_file(pid):
    """
    Parse the /proc/{pid}/maps file to find the heap address range
    Returns tuple of (start_address, end_address) for the heap
    """
    try:
        with open(f"/proc/{pid}/maps", 'r') as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    # Extract addresses from line
                    addresses = line.split()[0]
                    start_addr, end_addr = addresses.split('-')
                    return (int(start_addr, 16), int(end_addr, 16))
    except IOError as e:
        print(f"Error: Can't open maps file - {e}")
        sys.exit(1)

    print("Error: No heap found in the maps file")
    sys.exit(1)


def find_and_replace_in_memory(pid, start_address, end_address, search_bytes, replace_bytes):
    """
    Efficiently find and replace all occurrences of search_bytes in memory
    Returns the number of replacements made
    """
    mem_size = end_address - start_address
    try:
        with open(f"/proc/{pid}/mem", 'rb+') as mem_file:
            # Use memory mapping for more efficient access
            mem_file.seek(start_address)
            # Create memory map for the heap region
            mm = mmap.mmap(mem_file.fileno(), mem_size, offset=start_address)

            # Find all occurrences and replace
            count = 0
            position = mm.find(search_bytes)

            while position != -1:
                # Write the replacement
                mm.seek(position)
                mm.write(replace_bytes)
                count += 1

                # Find next occurrence
                mm.seek(position + len(search_bytes))
                next_chunk = mm.read(mem_size - position - len(search_bytes))
                next_pos = next_chunk.find(search_bytes)

                if next_pos == -1:
                    break
                position += len(search_bytes) + next_pos

            mm.close()
            return count

    except IOError as e:
        print(f"Error: Memory access failed - {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Memory mapping failed - {e}")
        sys.exit(1)


def main():
    """Main function to find and replace a string in the heap"""
    # Check arguments
    if len(sys.argv) != 4:
        print_usage_and_exit()

    # Parse arguments with error handling
    try:
        pid = int(sys.argv[1])
        search_string = sys.argv[2]
        replace_string = sys.argv[3]

        if not search_string:
            print("Error: Search string cannot be empty")
            print_usage_and_exit()

        # Get heap address range
        start_address, end_address = parse_maps_file(pid)

        # Prepare byte strings
        search_bytes = search_string.encode('utf-8')
        replace_bytes = replace_string.encode('utf-8')

        # Pad or truncate replace bytes to match search bytes length
        if len(replace_bytes) < len(search_bytes):
            replace_bytes += b'\0' * (len(search_bytes) - len(replace_bytes))
        else:
            replace_bytes = replace_bytes[:len(search_bytes)]

        # Find and replace all occurrences
        replacements = find_and_replace_in_memory(
            pid, start_address, end_address, search_bytes, replace_bytes)

        if replacements > 0:
            print(f"Successfully replaced {replacements} occurrence(s) in process {pid}")
        else:
            print(f"Error: String '{search_string}' not found in heap")
            sys.exit(1)

    except ValueError:
        print("Error: PID must be an integer")
        print_usage_and_exit()
    except PermissionError as e:
        print(f"Error: Permission denied - {e}")
        print("Note: This script requires root privileges to access process memory")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
