import os
from requests import post
from rgbprint import gradient_print, Color
import json
import hashlib
import time
import random
from console.utils import set_title
from console.utils import set_title
from tkinter import Tk, filedialog
import ctypes
import requests
import threading

def show_welcome_message():
    messages = [
        "🚀 Welcome to Dizzy Aio! 🚀",
        "🌟 Dizzy Aio by SpEc 🌟",
        "🔨 Unfinished, But Here It Is! 🔨",
        "🎁 Source Code Release 🎁",
        "😵 I Gave Up, You Got This! 😵",
    ]
    message = random.choice(messages)

    ctypes.windll.user32.MessageBoxW(0, 
        f"{message}\n\n"
        "I'm releasing the source code, I gave up, it isnt quite finished. But its a promising start! so feel free to use it. "
        "Remember to give credit if you skid! 😊", "Dizzy Aio by SpEc", 0)

def set_dizzy_aio_title():
    titles = [
        "🌀 Dizzy Aio | SpEc | Unfinished but Promising 🌀",
        "🌠 Dizzy Aio | SpEc | Always Improving 🌠",
        "🚀 Dizzy Aio | SpEc | Open Source Awesomeness 🚀",
        "🌟 Dizzy Aio | SpEc | Good Luck Skid! 🌟",
        "🎯 Dizzy Aio | SpEc | GIVE ME CREDIT! 🎯",
        "🌌 Dizzy Aio | SpEc | GIVE ME CREDIT! 🌌",
        "⚡ Dizzy Aio | SpEc | GIVE ME CREDIT! ⚡",
        "🔥 Dizzy Aio | SpEc | GIVE ME CREDIT! 🔥",
    ]

    def change_title():
        while True:
            for title in titles:
                set_title(title)
                time.sleep(1.5)  # Change title every 1.5 seconds

    title_thread = threading.Thread(target=change_title)
    title_thread.daemon = True
    title_thread.start()

# Example message
message = (
    "🎉 Welcome to the Dizzy Aio by SpEc! 🎉\n\n"
    "I created this tool, but I never quite finished it. It might not work as expected or could be outdated. "
    "I'm releasing the source code in case it's useful to someone. Please remember to give credit if you use it! 😊"
)


# Call the functions
show_welcome_message()
set_dizzy_aio_title()

# Define rainbow colors for the gradient
rainbow_colors = [
    Color(255, 0, 0), Color(255, 255, 0), Color(0, 128, 0),
    Color(0, 255, 255), Color(0, 0, 255), Color(255, 0, 255)
]

def get_hwid():
    drives = [drive for drive in os.popen("wmic logicaldisk get caption")]
    return hashlib.sha256(drives[0].encode()).hexdigest()

def authenticate():
    if os.path.exists('authkey.txt'):
        with open('authkey.txt', 'r') as file:
            key = file.read().strip()
    else:
        key = input("Hey Bozo! What's Your Cracked.io Authkey?")
        with open('authkey.txt', 'w') as file:
            file.write(key)

    hwid = get_hwid()

    try:
        url = "https://cracked.to/auth.php"
        payload = {'a': 'auth', 'k': key, 'hwid': hwid}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = post(url, data=payload, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            if 'error' in data:
                print(f"Error {data['error']}!")
                os.remove('authkey.txt')
                return False
            elif 'auth' in data:
                welcome_message = f"Welcome {data['username']}, enjoy your exclusive Cracked.to tool!"
                gradient_print(
                    welcome_message,
                    start_color=Color(255, 0, 0),
                    end_color=Color(0, 0, 255)
                )
                time.sleep(2)
                return True
    except Exception as ex:
        print(f"Error: {ex}")
        return False

def set_default_theme():
    global header_start_color, header_end_color
    header_start_color = Color(235, 51, 73)
    header_end_color = Color(244, 92, 67)

def set_sunset_theme():
    global header_start_color, header_end_color
    header_start_color = Color(255, 126, 95)
    header_end_color = Color(254, 180, 123)

def set_sea_blue_theme():
    global header_start_color, header_end_color
    header_start_color = Color(43, 88, 118)
    header_end_color = Color(78, 67, 118)

def set_aubergine_theme():
    global header_start_color, header_end_color
    header_start_color = Color(170, 7, 107)
    header_end_color = Color(97, 4, 95)

def set_celestial_theme():
    global header_start_color, header_end_color
    header_start_color = Color(195, 55, 100)
    header_end_color = Color(29, 38, 113)

# Initialize default theme
set_default_theme()

def print_header():
    header_text = r"""
 ____  _                 _____     _                 ____ _               _                  _       _       
|  _ \(_)_________   _  |_   _|__ | | _____ _ __    / ___| |__   ___  ___| | __    _        | | ___ (_)_ __  
| | | | |_  /_  / | | |   | |/ _ \| |/ / _ \ '_ \  | |   | '_ \ / _ \/ __| |/ /  _| |_   _  | |/ _ \| | '_ \ 
| |_| | |/ / / /| |_| |   | | (_) |   <  __/ | | | | |___| | | |  __/ (__|   <  |_   _| | |_| | (_) | | | | |
|____/|_/___/___|\__, |   |_|\___/|_|\_\___|_| |_|  \____|_| |_|\___|\___|_|\_\   |_|    \___/ \___/|_|_| |_|
                 |___/                                                                                       
                                                                                                               
Coded With ♥
    """
    gradient_print(header_text, start_color=header_start_color, end_color=header_end_color)

def check_tokens(tokens):
    try:
        for token in tokens:
            token = token.strip()
            response = post(f'https://discord.com/api/v6/invite/{token}', headers={'Authorization': token})
            if response.status_code == 401:
                print(f"{token} > Invalid")
            elif "You need to verify your account in order to perform this action." in str(response.content):
                print(f"{token} > Phone lock")
            else:
                print(f"{token} > Valid")
    except Exception as e:
        print(f"Error: {e}")

def discord_generate():
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
    }
    payload = '{"content": "!d bump"}'
    tokens = []

    for i in range(5):  # Generate 5 tokens
        captcha_key = solve_captcha()
        if captcha_key is not None:
            response = post("https://discord.com/api/v9/channels/830913283866384710/messages", headers=headers, data=payload)

            if response.status_code == 200:
                token = response.json()["token"]
                tokens.append(token)
                print(f"Generated token: {token}")
            else:
                print(f"Error generating token (status code: {response.status_code})")

    return tokens

def solve_captcha():
    def payload(service="capsolver.com", proxy=None, user_agent=None):
        p = {
            "clientKey": keyCap,
            "task": {
                "websiteURL": "https://discord.com/",
                "websiteKey": "4c672d35-0701-42b2-88c3-78380b0db560",
            }
        }
        if service == "capsolver.com":
            p['appId'] = "E68E89B1-C5EB-49FE-A57B-FBE32E34A2B4"
            p['task']['type'] = "HCaptchaTurboTask"
            p['task']['proxy'] = proxy
            p['task']['userAgent'] = user_agent
        if service == "capmonster.cloud":
            p['task']['type'] = "HCaptchaTask"
            p['task']['proxyType'] = "http"
            p['task']['proxyAddress'] = proxy.split("@")[1].split(":")[0]
            p['task']['proxyPort'] = proxy.split("@")[1].split(":")[1]
            p['task']['proxyLogin'] = proxy.split("@")[0].split(":")[0]
            p['task']['proxyPassword'] = proxy.split("@")[0].split(":")[1]
        return p

    r = requests.post(f"https://api.capsolver.com/createTask", json=payload("capsolver.com", proxy,
                                                                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'))
    try:
        if r.json().get("taskId"):
            taskid = r.json()["taskId"]
        else:
            return None
    except:
        print("Couldn't retrieve captcha task id.", r.text, "failed")
        return None

    # Waiting for results
    while True:
        try:
            r = requests.post(f"https://api.capsolver.com/getTaskResult",
                              json={"clientKey": keyCap, "taskId": taskid})
            if r.json()["status"] == "ready":
                key = r.json()["solution"]["gRecaptchaResponse"]
                return key
            elif r.json()['status'] == "failed":
                return None
        except:
            print("Failed to get solving status.", r.text, "failed")
            return None

def generate_discord_tokens():
    global total, locked, unlocked
    try:
        tokens = discord_generate()
        total += len(tokens)
        unlocked += len(tokens)

        with open('tokens.txt', 'a') as file:
            for token in tokens:
                file.write(f'{token}\n')

        print(f'Successfully saved {len(tokens)} tokens to tokens.txt')

        with open('output.txt', 'a') as file:
            file.write(f'Generated {len(tokens)} tokens\n')

        input("Press Enter to return to the menu...")
    except Exception as e:
        log_error(f'Error generating tokens: {str(e)}')
        print("An error occurred while generating tokens. Check output.txt for details.")
        input("Press Enter to return to the menu...")


def check_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_names_bios():
    names = []
    bios = []
    if config['names']:
        try:
            with open('names.txt', 'r') as file:
                names = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass
    
    if config['bios']:
        try:
            with open('bios.txt', 'r') as file:
                bios = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass
    
    return names, bios

def load_avatars():
    avatars = []
    if config['avatar']:
        check_directory('avatar')
        for file in os.listdir('avatar'):
            if file.endswith(".jpg") or file.endswith(".png"):
                avatars.append(file)
    return avatars

def get_random_name(names):
    return random.choice(names)

def get_random_bio(bios):
    return random.choice(bios)

def get_random_avatar(avatars):
    return random.choice(avatars)

def join_servers(tokens, invite_code):
    names, bios = load_names_bios()
    avatars = load_avatars()

    try:
        for token in tokens:
            token = token.strip()
            response = post(f'https://discord.com/api/v6/invite/{invite_code}', headers={'Authorization': token})
            if response.status_code == 401:
                print(f"{token} > Invalid")
            elif "You need to verify your account in order to perform this action." in str(response.content):
                print(f"{token} > Phone lock")
            else:
                if config['avatar']:
                    avatar = get_random_avatar(avatars)
                    print(f"{token} > Joined | Avatar: {avatar}")
                else:
                    print(f"{token} > Joined")
                if config['names'] and config['bios']:
                    name = get_random_name(names)
                    bio = get_random_bio(bios)
                    print(f"    Name: {name}\n    Bio: {bio}")
                elif config['names']:
                    name = get_random_name(names)
                    print(f"    Name: {name}")
                elif config['bios']:
                    bio = get_random_bio(bios)
                    print(f"    Bio: {bio}")
    except Exception as e:
        log_error(f'Error joining servers: {str(e)}')


def main_menu():
    if not authenticate():
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print_header()

        gradient_print("[+] 1. Check Tokens", start_color=header_start_color, end_color=header_end_color)
        gradient_print("[+] 2. Join Servers", start_color=header_start_color, end_color=header_end_color)
        gradient_print("[+] 3. Generate Discord Tokens", start_color=header_start_color, end_color=header_end_color)
        gradient_print("[+] 4. Change Theme", start_color=header_start_color, end_color=header_end_color)
        gradient_print("[+] 5. Exit", start_color=header_start_color, end_color=header_end_color)

        choice = input("Enter your choice: ")
        if choice == '1':
            Tk().withdraw()  # Prevent a root window from appearing
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, "r") as file:
                    tokens = file.readlines()
                check_tokens(tokens)
                input("Press Enter to continue...")
        elif choice == '2':
            Tk().withdraw()  # Prevent a root window from appearing
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if file_path:
                invite_code = input("Enter the invite code (R1xa78h4): ")
                with open(file_path, "r") as file:
                    tokens = file.readlines()
                join_servers(tokens, invite_code)
                input("Press Enter to continue...")
        elif choice == '3':
            generate_discord_tokens()  # Call the function to generate tokens
            input("Press Enter to continue...")
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            print_header()
            gradient_print("[+] 1. Default", start_color=header_start_color, end_color=header_end_color)
            gradient_print("[+] 2. Sunset", start_color=header_start_color, end_color=header_end_color)
            gradient_print("[+] 3. Sea Blue", start_color=header_start_color, end_color=header_end_color)
            gradient_print("[+] 4. Aubergine", start_color=header_start_color, end_color=header_end_color)
            gradient_print("[+] 5. Celestial", start_color=header_start_color, end_color=header_end_color)
            theme_choice = input("Enter your choice: ")
            if theme_choice == '1':
                set_default_theme()
            elif theme_choice == '2':
                set_sunset_theme()
            elif theme_choice == '3':
                set_sea_blue_theme()
            elif theme_choice == '4':
                set_aubergine_theme()
            elif theme_choice == '5':
                set_celestial_theme()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def log_error(error_message):
    with open('output.txt', 'a') as file:
        file.write(f'Error: {error_message}\n')

if __name__ == "__main__":
    # Create config file if it doesn't exist
    if not os.path.exists('config.json'):
        default_config = {
            "capsolver-key": "",
            "avatar": True,
            "hypesquad": True,
            "bio": True,
            "invite": ""
        }
        with open('config.json', 'w') as config_file:
            json.dump(default_config, config_file)

    # Load CAPTCHA solver configurations
    captcha_config = json.load(open('config.json', 'r'))
    keyCap = captcha_config.get('capsolver-key', '')

    total = 0
    locked = 0
    unlocked = 0

    main_menu()
