from colorama import Fore
import os
import requests
import sys
import random
import time

def bannnner():
	print('''
           _           _                                    _
  __ _  __| |_ __ ___ (_)_ __        _ __   __ _ _ __   ___| |
 / _` |/ _` | '_ ` _ \| | '_ \ _____| '_ \ / _` | '_ \ / _ \ |
| (_| | (_| | | | | | | | | | |_____| |_) | (_| | | | |  __/ |
 \__,_|\__,_|_| |_| |_|_|_| |_|     | .__/ \__,_|_| |_|\___|_|
                                    |_|
	''')
# mohammad javad nikbakht

os.system('cls' or 'clear')

bannnner()

def mjn():
    try:
        
        url = input(Fore.LIGHTGREEN_EX+"Enter WebSite Address [>>] ")
        list_=['admin/','administrator/','login.php','administration/','admin1/','admin2/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','login.aspx',
'admin_area/admin.asp','power-of-black-team','admin_area/login.asp','admin/account.html','Components/SiteMember/Admin/Login.aspx','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html']

        url = ('http://'+url+"/")
        for i in list_:
            pobt = requests.get(url+i)
            if pobt.status_code == 200:
                print(Fore.LIGHTGREEN_EX+"[+] "+url+i+" Found")
            else:
                print(Fore.LIGHTRED_EX+"[-] "+url+i+" Not Found")
    except:
        print("check internet or url or you :)")


mjn()
print(Fore.LIGHTGREEN_EX+'')