import requests
import random
import time
import string
from colorama import Fore
from colorama import Style
import os


lower_case = "qwertzuiopasdfghjklyxycvbnm"
upper_case = "QWERTZUIOPASDFGHJKLYXCVBNM"

Use_for = lower_case + upper_case + string.digits * 2
length_for_link = 16
print(f"{Fore.LIGHTCYAN_EX}Hello! And welcome to my nitro generator, this it the most special way to generate nitro... Have fun using it!")
num = int(input(f"Input How Many Codes to Generate and Check:{Fore.RESET}\n"))


with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    os.system("cls")


    for i in range(num):
        code = "".join(random.sample(Use_for, length_for_link))
        url = (f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
        responsecode = requests.get(url)
        while responsecode.status_code == 429:
            responsecode = requests.get(url)
            print(f"{Fore.LIGHTRED_EX}Response code: {responsecode}, too many requests{Fore.RESET}")
            print(f"{Fore.LIGHTYELLOW_EX}Reconnecting to the website...{Fore.RESET}")
            time.sleep(5)
            if responsecode.status_code == 404:
                print(f"{Fore.LIGHTGREEN_EX}Response code: {responsecode} | Website loading in...")
            if responsecode.status_code != 429:
                pass
                print(f"{Fore.LIGHTGREEN_EX}Connection success...{Fore.RESET}")
                time.sleep(0.2)
        if responsecode.status_code == 200:
            print(f'{Fore.LIGHTGREEN_EX}Valid code found!{Fore.RESET}')
            print(f"\n\n {Fore.LIGHTGREEN_EX}Valid {Fore.RESET}| https://discord.gift/{code}\n\n")
            print(f"{Fore.LIGHTBLUE_EX}Transfroming it into the txt file...{Fore.RESET}")
            validcode = f"https://discord.gift/{code}"
            file.write(validcode)
            print(f"{Fore.LIGHTMAGENTA_EX}Transfromation done, enjoy your nitro{Fore.RESET}")
            exit()
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid {Fore.RESET}| https://discord.gift/{code}")
