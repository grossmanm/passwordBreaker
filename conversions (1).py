#!/usr/bin/env python3
import hashlib
import binascii
import time
t1 = time.clock()
file = open('passwords2.txt','w')
words = [line.strip().lower() for line in open('words.txt')]
passwords = []
tempPasswords = [line.strip().lower() for line in open('pass2.txt')]
# Compute the MD5 hash of this example password
hexes = []
for i in tempPasswords:
    t = i.split(':')
    passwords.append([t[0],t[1]])
for i in passwords:
    hex = i[1].split('$')
    i[1] = hex[1]
    hexes.append(hex[0])

# Compute the MD5 hash of this example password
numpass = 0
cracked =0
for i in range(len(passwords)):
    for password in words:
        pas = hexes[i] + password
        encodedPassword = pas.encode('utf-8') # type=bytes

        md5 = hashlib.md5(encodedPassword)
        passwordHash = md5.digest() # type=bytes


        passwordHashAsHex = binascii.hexlify(passwordHash) # weirdly, still type=bytes

        passwordHashAsHexString = passwordHashAsHex.decode('utf-8') # type=string
        numpass += 1
        if passwordHashAsHexString == passwords[i][1]:
            cracked +=1
            pas = str(passwords[i][0]) + ':' + str(password)
            file.write(pas + '\n')
            break
t2 = time.clock()
print("passwords cracked: " + str(cracked))
print("passwords tried: " + str(numpass))
print("number of password candidates checked per second: " + str(numpass / (t2 - t1)))
print("total time: " + str(t2 - t1))