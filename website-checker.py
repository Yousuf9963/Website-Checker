import os

os.system("pip install requests")
os.system("clear")


print("[+] Tool Name:Website-Checker")

print("[+] Author:Yousuf Shafi'i Muhammad. Junior Programmer")

print("[+] Version:1.0")

print("[+] Team:Junior Programmers")

print("[+] Github:https://github.com/Yousuf9963/Cam-Ethical-Hackers")

print("[+] Follow me on Github: https://github.com/Yousuf9963")

print("[-] Website: muhammadabdirahman.wixsite.com/yousuf9963blog.")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

print("[+] Motto: I hope for you good future and i am willing that you will come high effort.")

print("")

import requests

print("Enter Website With 'https://wwww' Example: https://www.examplewebsite.com")

url = input("Enter Website to Check is Valid or Invalid: ")

try:

    response = requests.get(url)

    if response.status_code == 200:

        print("The website is valid")

    else:

        print("The website is invalid")

except:

    print("The website is invalid")

os.system("xdg-open https://chat.whatsapp.com/IcFWDRiYVBx7nAxc0VIAzl")
