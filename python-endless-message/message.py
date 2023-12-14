import pyautogui
import time
import os


count = int(input("Göndermek istediğiniz mesaj sayısını giriniz: "))
message = input("Mesajı giriniz:")
endMessage = input("İstiyosanız Bitiş mesajı giriniz")

n = 10

print("Spam bot" , n , "saniyede başlıyor")

while n > 0:
    print(n)
    n -= 1
    time.sleep(1)
    os.system("cls")

print("Spam bot başladı")


def send(message):
    pyautogui.typewrite(message)
    pyautogui.press("Enter")


while count:
    send(message)
    time.sleep(0.1)
    count -= 1


send(endMessage)

os.system("cls")

print("Spam bot durdu")