# import pywhatkit as kit
# import time
# import schedule

# def send_hello():
#     kit.sendwhatmsg_instantly("+919328935727","hello",wait_time=15)
# schedule.every(1).minutes.do(send_hello)

# while True:
#     send_hello()
#     time.sleep(30)

import time
import webbrowser

phone_number = "+919328935727"  # 
message = "HELLO"
url = f"https://web.whatsapp.com/send?phone={+919328935727}&text={"hello"}"

def send_hello():
    webbrowser.open(url)  
    time.sleep(10)  
    print("Message opened, please press Enter manually if needed.")

while True:
    send_hello()
    time.sleep(30)  

