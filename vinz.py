import json
from urllib import request
import base64
from os import system
from time import sleep
from requests.api import get
system('cls||clear')
print("==============================")
print("==>   CHECK ORDER STATUS   <==")
print("==============================")
order_id = str(input('ORDER ID : '))
print("==============================")
print("Checking Order ID...")
print("==============================")
try:
    server= ("https://api.iamvinz.com/api/ig-pointer?id=" +order_id)
    apikey= ("&apikey=iamvinz")
    url= (server + apikey)
    response = request.urlopen(url)
    data = json.loads(response.read())
    get_status= (f"{data['status']}")
    get_followers= (f"{data['remains']}")
    get_server= (f"{data['server']}")
    get_id= (f"{data['id_order']}")
    get_sisa= (f"{data['remains']}")
    system("cls||clear")
    print("=============================")
    print("==>      ORDER STATUS     <==")
    print("=============================")
    print("SV :" + get_server)
    print("=============================")
    print("")
    print("ID : " + get_id)
    print("STATUS : " + get_status)
    print("REMAINS : "+ get_sisa)
    print("")
    print("=============================")
    print("      (C)2021 VinzCloud      ")
    print("=============================")
except Exception:
    system("cls||clear")
    cek_id_error= (f"{data['error']}")
    print("=============================")
    print("==>      ORDER STATUS     <==")
    print("=============================")
    print("")
    print("Oops, Checking Failed !")
    print(cek_id_error+ ", Please Check Your Order ID Is Correct !")
    print("")
    print("=============================")
    print("      (C)2021 VinzCloud      ")
    print("=============================\n\n")
