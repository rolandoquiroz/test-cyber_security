#!/usr/bin/python3
"""
read_write_heap.py - Script to search and replace a string in the heap of a running process.
Usage:
    python3 read_write_heap.py pid search_string replace_string
Arguments:
    pid - Process ID of the target process
    search_string - ASCII string to search for in the heap
    replace_string - ASCII string to replace the search_string
"""
import sys


def find_and_replace_in_heap(pid, search_string, replace_string):
    """
    Find and replace a string in the heap memory of a running process.
    Parameters:
        pid: Process ID of the target process
        search_string: String to search for in the heap (as bytes)
        replace_string: String to replace the search_string (as bytes)
    """
    try:
        # Open and read the memory maps to find the heap
        maps_path = f"/proc/{pid}/maps"
        with open(maps_path, 'r') as maps_file:
            heap_region = None
            for line in maps_file:
                if "[heap]" in line:
                    heap_region = line
                    break

            if not heap_region:
                print(f"No heap found for process {pid}")
                sys.exit(1)

            # Extract heap address range
            addr_range = heap_region.split()[0]
            start_addr, end_addr = addr_range.split('-')
            start_addr = int(start_addr, 16)
            end_addr = int(end_addr, 16)

        # Open process memory and perform the replacement
        mem_path = f"/proc/{pid}/mem"
        with open(mem_path, 'rb+') as mem_file:
            # Read heap content
            mem_file.seek(start_addr)
            heap_content = mem_file.read(end_addr - start_addr)

            # Find all occurrences of the search string
            offset = heap_content.find(search_string)
            if offset == -1:
                print(f"String '{search_string.decode('ascii', errors='replace')}' not found in heap")
                sys.exit(1)

            # Prepare replacement data
            if len(replace_string) < len(search_string):
                # Pad with null bytes if replacement is shorter
                padded_replace = replace_string + b'\0' * (len(search_string) - len(replace_string))
            else:
                # Truncate if replacement is longer
                padded_replace = replace_string[:len(search_string)]

            # Write the replacement
            mem_file.seek(start_addr + offset)
            mem_file.write(padded_replace)
            print("SUCCESS!")

    except PermissionError:
        print(f"Permission denied. Try running the script with sudo.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Process with PID {pid} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to handle input arguments and execute the heap string replacement.
    """
    # Check argument count
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} pid search_string replace_string")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Invalid PID. Please provide an integer.")
        sys.exit(1)

    # Check for empty search string
    if not sys.argv[2]:
        print("Search string cannot be empty")
        sys.exit(1)

    search_string = sys.argv[2].encode('ascii')
    replace_string = sys.argv[3].encode('ascii')

    find_and_replace_in_heap(pid, search_string, replace_string)


if __name__ == "__main__":
    main()
