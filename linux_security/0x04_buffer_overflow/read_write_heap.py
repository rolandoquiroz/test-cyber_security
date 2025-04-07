#!/usr/bin/python3
"""
Script to modify a string in the heap memory of a running process.
This script finds a target string in the heap of a process and replaces it with a new string.

Usage: ./script.py pid search_string replace_string
"""
import sys
import os


def print_usage_and_exit():
    """Print usage information and exit with status code 1"""
    print(f"Usage: {sys.argv[0]} pid search_string replace_string")
    sys.exit(1)


def find_heap_memory_range(pid):
    """
    Find the heap memory address range for a process

    Args:
        pid (str): Process ID

    Returns:
        tuple: (start_address, end_address) of heap memory

    Raises:
        FileNotFoundError: If the process maps file doesn't exist
        ValueError: If heap section isn't found
    """
    maps_path = f"/proc/{pid}/maps"

    try:
        with open(maps_path, "r") as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    # Extract address range from the line
                    address_range = line.split()[0]
                    start_addr, end_addr = address_range.split("-")
                    return int(start_addr, 16), int(end_addr, 16)
    except FileNotFoundError:
        print(f"Error: Process {pid} not found or permission denied")
        sys.exit(1)

    # If we reach here, the heap wasn't found
    print(f"Error: No heap memory found for process {pid}")
    sys.exit(1)


def replace_string_in_heap(pid, search_bytes, replace_bytes):
    """
    Find and replace a string in process heap memory

    Args:
        pid (str): Process ID
        search_bytes (bytes): Bytes to search for
        replace_bytes (bytes): Bytes to replace with

    Returns:
        bool: True if replacement was successful
    """
    # Find heap memory range
    start_addr, end_addr = find_heap_memory_range(pid)

    # Ensure replace_bytes is padded or truncated to match search_bytes length
    if len(replace_bytes) < len(search_bytes):
        replace_bytes = replace_bytes.ljust(len(search_bytes), b'\x00')
    else:
        replace_bytes = replace_bytes[:len(search_bytes)]

    # Open process memory
    mem_path = f"/proc/{pid}/mem"
    try:
        with open(mem_path, "r+b") as mem_file:
            # Read heap memory
            mem_file.seek(start_addr)
            heap_data = mem_file.read(end_addr - start_addr)

            # Find target string
            position = heap_data.find(search_bytes)
            if position == -1:
                print(f"Error: String '{search_bytes.decode(errors='replace')}' not found in heap")
                sys.exit(1)

            # Write replacement string
            target_addr = start_addr + position
            mem_file.seek(target_addr)
            mem_file.write(replace_bytes)

            return True
    except (PermissionError, FileNotFoundError):
        print(f"Error: Cannot access memory for process {pid}. Are you running as root?")
        sys.exit(1)
    except IOError as e:
        print(f"Error accessing process memory: {e}")
        sys.exit(1)


def main():
    """Main function - parse arguments and call helper functions"""
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print_usage_and_exit()

    # Parse arguments
    try:
        pid = sys.argv[1]
        search_string = sys.argv[2]
        replace_string = sys.argv[3]

        # Validate arguments
        if not search_string:
            print("Error: Search string cannot be empty")
            print_usage_and_exit()

        # Convert strings to bytes
        search_bytes = search_string.encode()
        replace_bytes = replace_string.encode()

        # Perform replacement
        if replace_string_in_heap(pid, search_bytes, replace_bytes):
            print("SUCCESS!")

    except ValueError as e:
        print(f"Error: {e}")
        print_usage_and_exit()


if __name__ == "__main__":
    main()
