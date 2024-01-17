from urllib.request import urlopen
import hashlib

sha3hash = input('Enter SHA-3 (SHA3-512) Hash value: ')

try:
    password_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')

    for password in password_list.split('\n'):
        guess = hashlib.sha3_512(bytes(password, 'utf-8')).hexdigest()

        if guess == sha3hash:
            print("[+] The password is: " + str(password))
            break
        else:
            print("The password does not match in the list...")

except Exception as exc:
    print('There was a problem: %s' % (exc))