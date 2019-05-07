#!/usr/bin/env python3
import hashlib
import binascii
import time
t1 = time.clock()
words = [line.strip().lower() for line in open('words.txt')]
passwords = []
tempPasswords = [line.strip().lower() for line in open('pass1.txt')]
for i in tempPasswords:
    t = i.split(':')
    passwords.append([t[0],t[1]])
# Compute the MD5 hash of this example password
numpass =0
passwordHashAsHexStrings = []
file = open('passwords1.txt','w')
for password in words:
    encodedPassword = password.encode('utf-8') # type=bytes

    md5 = hashlib.md5(encodedPassword)
    passwordHash = md5.digest() # type=bytes

    passwordHashAsHex = binascii.hexlify(passwordHash) # weirdly, still type=bytes

    passwordHashAsHexString = passwordHashAsHex.decode('utf-8') # type=string
    passwordHashAsHexStrings.append([password,passwordHashAsHexString])

cracked = 0
for i in passwords:
    for j in passwordHashAsHexStrings:
        numpass +=1
        if j[1] == i[1]:
            cracked += 1
            pas = str(i[0]) + ':' + str(j[0])
            file.write(pas + '\n')
            break
t2 = time.clock()
print("passwords cracked: " + str(cracked))
print("passwords tried: " + str(numpass))
print("number of password candidates checked per second: " + str(numpass / (t2 - t1)))
print("total time: " + str(t2 - t1))
