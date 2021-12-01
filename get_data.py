#! /usr/bin/env python3

"""
Script for getting input data from aoc website, for Chrome/Mac
Uses year and day input, only pings aoc if input file doesn't exist
Utilises local cookie storage onsqlite
"""
import os
from sqlite3.dbapi2 import connect
import pathlib

# needed for decrypting encrypted_value of aoc session cookie
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

# needed for accessing local sqlite Cookies file
import sqlite3

# needed for accessing keychain password on Mac
import keyring

# needed for curl requesting from python script
import requests

# function to get rid of padding
def clean(x): 
    return x[:-x[-1]].decode('utf8')

# function to get session cookie from local files
def get_session_cookie():
    db_path = f"{os.path.expanduser('~')}/Library/Application Support/Google/Chrome/Default/Cookies"
    with sqlite3.connect(db_path) as db:
        cursor = db.execute("SELECT encrypted_value FROM cookies WHERE host_key='.adventofcode.com' AND name='session'")
    return cursor.fetchone()[0]

def main(year, day, file_location):
    # replace with your encrypted_value from sqlite3
    encrypted_value = get_session_cookie() 

    # trim off the 'v10' that Chrome/ium prepends
    encrypted_value = encrypted_value[3:]

    # default values used by both Chrome and Chromium in OSX and Linux
    salt = b'saltysalt'
    iv = b' ' * 16
    length = 16

    # on Mac, replace MY_PASS with your password from Keychain
    my_pass = keyring.get_password('Chrome Safe Storage', 'Chrome')
    my_pass = my_pass.encode('utf8')

    # 1003 on Mac, 1 on Linux
    iterations = 1003

    key = PBKDF2(my_pass, salt, length, iterations)
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    decrypted = clean(cipher.decrypt(encrypted_value))

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie":"session=" + decrypted}

    try:
        res = requests.get(url=url, headers=headers)
    except:
        print("error fetching input")

    # write content to input.txt file
    content = res.content
    if content == b"404 Not Found\n":
        print("404, likely incorrect year and day combo")
    else:
        file.mkdir(parents=True, exist_ok=True)
        with open(file / "input.txt", "wb") as f:
            f.write(content)

if __name__ == "__main__":

    year = input("Enter Year:")
    day = input("Enter Day:")

    file = pathlib.Path(f"{os.path.dirname(os.path.abspath(__file__))}/{year}/{day}")
    if not (file / "input.txt").exists():
        main(year, day, file)
    else:
        print("input.txt already exists for this year and day")
