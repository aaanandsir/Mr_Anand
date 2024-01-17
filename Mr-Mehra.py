import requests
import json
import time
import logging
import socket
import sys
from platform import system
import random
import os
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup

API_VERSION = 'v15.0'

HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

brown_text = "\033[0;33m"
yellow_text = "\033[1;33m"
red_text = "\033[1;31m"
green_text = "\033[1;32m"
cyan_text = "\033[1;36m"
blue_text = "\033[1;34m"
magenta_text = "\033[1;35m"
pink_text = "\033[1;38;5;206m"  # Pink
purple_text = "\033[1;38;5;90m"  # Purple
golden_text = "\033[1;38;5;178m"  # Golden
teal_text = "\033[1;38;5;30m"  # Teal
orange_text = "\033[1;38;5;208m"  # Orange
midnight_blue_text = "\033[1;38;5;17m"  # Midnight Blue
khaki_text = "\033[1;38;5;185m"  # Khaki
coral_text = "\033[1;38;5;209m"  # Coral
reset_text = "\033[0m"

additional_logo = f"""
{midnight_blue_text}
            â£€â£€â£¤â£¤
                  â¢€                                 
{reset_text}
"""

logo = f"""
{teal_text}
_______

{reset_text}
"""

made_by_text = f"{orange_text}HATERS KI BAHAN KI...KAIR CHHODO JANE DO ðŸ˜Ž{reset_text}"
def main_apv():
    os.system('clear')
    ak="PRINCE"
    name = input(f"Enter your Name :")
    email = input(f"Enter your Email :")
    print(logo)
    try:
        key1=open('/data/data/com.termux/files/usr/bin/.MEHRA-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print ("[*]_______________________")
        print ("  Your Token Is Not Approved Already")
        print ("[*]_______________________")
        print ("           THIS TOOL IS PAID ")
        print ("           THIS IS YOUR KEY BRO")
        print ("[*]_______________________")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid)
        print ("[*]_______________________")
        kok=open('/data/data/com.termux/files/usr/bin/.Prince-cov', 'w')
        kok.close()
        print ("")
        print ("")
        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("[*]_______________________")
        time.sleep(6)
        os.system("xdg-open https://wa.me/+917643890954")
    r1=requests.get("https://github.com/Prince04630/blob/main/Approval.txt"). text

    if key1 in r1:
    	#R ke jaga apne main jahan sy script started krna chahty wo lagao 
         main()
    else:
        print(logo)
        print ("[*]_______________________")
        print ("  Your Token is not approved  ")
        print ("[*]_______________________")
        print ("THIS IS YOUR KEY BRO")
        print ("[*]FIRST APPROVAL KEY THEN RUN")
        print ("")
        print ("          YOUR KEY : "+ak+key1)
        print ("[*]_______________________")
        print ("     Copy Key And Sent Me WP Approvel Your Key ")
        print ("[*]_______________________")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+email+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+key1
		
        os.system('am start https://wa.me/+917643890954?text=' + tks)
      
os.system('clear')
		

def is_internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        pass
    return False

def get_user_name(access_token):
    try:
        response = requests.get(f'https://graph.facebook.com/{API_VERSION}/me', params={'access_token': access_token})
        response.raise_for_status()
        user_data = response.json()
        return user_data.get('name', 'Unknown User')
    except requests.exceptions.RequestException as e:
        logging.error(f"{red_text}Error fetching user name: {e}{reset_text}")
        return 'Unknown User'

def send_message(api_url, access_token, thread_id, message):
    parameters = {'access_token': access_token, 'message': message}
    try:
        response = requests.post(api_url, data=parameters, headers=HEADERS)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"{red_text}Error sending message: {e}{reset_text}")
        return None

def get_colored_input(prompt, color_code):
    user_input = input(f"{color_code}{prompt}{reset_text}")
    return user_input

def print_brown(text):
    print(f"{brown_text}{text}{reset_text}")

def print_yellow(text):
    print(f"{yellow_text}{text}{reset_text}")

def print_red(text):
    print(f"{red_text}{text}{reset_text}")

def print_green(text):
    print(f"{green_text}{text}{reset_text}")

def print_cyan(text):
    print(f"{cyan_text}{text}{reset_text}")

def print_blue(text):
    print(f"{blue_text}{text}{reset_text}")

def print_magenta(text):
    print(f"{magenta_text}{text}{reset_text}")

def print_pink(text):
    print(f"{pink_text}{text}{reset_text}")

def print_purple(text):
    print(f"{purple_text}{text}{reset_text}")

def print_golden(text):
    print(f"{golden_text}{text}{reset_text}")

def print_teal(text):
    print(f"{teal_text}{text}{reset_text}")

def print_orange(text):
    print(f"{orange_text}{text}{reset_text}")

def print_midnight_blue(text):
    print(f"{midnight_blue_text}{text}{reset_text}")

def print_khaki(text):
    print(f"{khaki_text}{text}{reset_text}")

def print_coral(text):
    print(f"{coral_text}{text}{reset_text}")

def get_access_tokens():
    choice = get_colored_input("Press 1 to input access tokens from a file, Press 2 for manual input: ", pink_text)

    if choice == '1':
        try:
            file_path = get_colored_input("Enter the file path containing access tokens: ", magenta_text)
            with open(file_path, 'r') as file:
                access_tokens = file.read().splitlines()
        except FileNotFoundError:
            print_red(f"{red_text}File not found. Please provide a valid file path.{reset_text}")
            exit()
    elif choice == '2':
        num_tokens = int(get_colored_input("Enter the number of access tokens: ", purple_text))
        access_tokens = [get_colored_input(f"Enter access token {i + 1}: ", golden_text) for i in range(num_tokens)]
    else:
        print_red(f"{red_text}Invalid choice. Exiting.{reset_text}")
        exit()

    return access_tokens

def get_thread_ids():
    choice = get_colored_input("Press 1 to input thread IDs from a file, Press 2 for manual input: ", khaki_text)

    if choice == '1':
        try:
            file_path = get_colored_input("Enter the file path containing thread IDs: ", coral_text)
            with open(file_path, 'r') as file:
                thread_ids = file.read().splitlines()
        except FileNotFoundError:
            print_red(f"{red_text}File not found. Please provide a valid file path.{reset_text}")
            exit()
    elif choice == '2':
        num_threads = int(get_colored_input("Enter the number of thread IDs: ", khaki_text))
        thread_ids = [get_colored_input(f"Enter thread ID {i + 1}: ", coral_text) for i in range(num_threads)]
    else:
        print_red(f"{red_text}Invalid choice. Exiting.{reset_text}")
        exit()

    return thread_ids

def get_access_tokens_and_thread_ids():
    access_tokens = get_access_tokens()
    thread_ids = get_thread_ids()
    return access_tokens, thread_ids

def round_robin_send_messages(access_tokens, thread_ids, messages, mn, sleep_time):
    ist = pytz.timezone('Asia/Kolkata')

    num_tokens = len(access_tokens)
    num_threads = len(thread_ids)
    num_messages = len(messages)
    current_message_index = 0

    while True:
        for j in range(num_tokens):
            access_token = access_tokens[j]
            user_name = get_user_name(access_token)

            for k in range(num_threads):
                thread_id = thread_ids[k]
                api_url = f'https://graph.facebook.com/{API_VERSION}/t_{thread_id}/'
                current_message = messages[current_message_index]
                message = f'{mn} {current_message}'

                response = send_message(api_url, access_token, thread_id, message)
                current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

                if response and response.status_code == 200:
                    print_green(f"[âœ“]{user_name} Sir Messag send of this this Rascals ->>({thread_id})â€ºÂ»FUCK THAT MOTHERFUCKERðŸ–•______: ({mn}) {message} - Time: {current_time}__________________")
                else:
                    print_red(f"{red_text}Failed to send message ANAND SIR PLEASE HELP {user_name} to thread {thread_id}: {message}{reset_text}")

                sleep(sleep_time)

        current_message_index = (current_message_index + 1) % num_messages

def main():
    print_blue(additional_logo)
    print_yellow(logo)
    print_yellow(made_by_text)
    logging.basicConfig(level=logging.INFO)

    while True:
        try:
            while not is_internet_available():
                print_red(f"Internet connection not available. Waiting for connection...")
                sleep(10)

            access_tokens, thread_ids = get_access_tokens_and_thread_ids()
            mn_color = get_colored_input("Enter your haters name: ", purple_text)
            txt_file_path = get_colored_input("Enter the path to your message file (txt): ", golden_text)

            try:
                with open(txt_file_path, 'r') as file:
                    messages = file.read().splitlines()
            except FileNotFoundError:
                print_red(f"{red_text}File not found. Please provide a valid file path.{reset_text}")
                exit()

            sleep_time = float(get_colored_input("Enter the time delay between messages (in seconds): ", teal_text))

            round_robin_send_messages(access_tokens, thread_ids, messages, mn_color, sleep_time)

        except KeyboardInterrupt:
            logging.info(f"{brown_text}\nScript terminated by user.{reset_text}")

if __name__ == "__main__":
    main_apv()
