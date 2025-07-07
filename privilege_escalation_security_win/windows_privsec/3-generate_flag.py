import hashlib

def gen_flag(username):
    return hashlib.md5(('L0K8H7I6G5F4E3D2' + username).encode()).hexdigest()

print(gen_flag("rolandoquiroz"))   # 4b77762af53be75857300268abd37007
