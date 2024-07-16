import time
import pyautogui
from PIL import ImageGrab # 듀얼 모니터 pyautogui 설정
from functools import partial # 듀얼 모니터 pyautogui 설정
import glob

from ppadb.client import Client as AdbClient
import time

#앱플레이어 연결

# deviceport = 5554

# #adb settings
# adb = AdbClient(host="127.0.0.1", port=5037)
# devices = adb.devices()
# if not devices:
#     print("디바이스를 찾을 수 없습니다.")
#     quit()
# device = devices[0]

# if devices is not None:
#     print("Adb detected")
# else:
#     print("Adb not detected")
#     exit(0)

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True) # 듀얼 모니터 pyautogui 설정

# img_capture = pyautogui.locateOnScreen("./img/test1.jpg" , confidence=0.5) # 50%
# #이미지 클릭

# pyautogui.click(img_capture)

# count = 0 # 광고 시청 횟수

# while count< 20 : # 원하는 횟수 지정

#     img_capture1 = pyautogui.locateCenterOnScreen("./img/test1.jpg" , confidence=0.7) # 클릭 버튼
#     if type(img_capture1) != type(None) : # 이미지를 찾았으면 아래코드 진행
#         print("있다 클릭")
#         pyautogui.click(img_capture1)
#         time.sleep(1)
#         count += 1
#         continue   




path = "./*"
file_list = glob.glob(path)
file_list_py = [file for file in file_list if file.endswith(".py")]

print ("file_list_py: {}".format(file_list_py))


filter_img = file_list_py

my_img = filter_img

def click() :
 Turn = 0
 while Turn< 20 :
    try:
        img_capture1 = pyautogui.locateCenterOnScreen(my_img , confidence=0.7)          
        print(img_capture1)
        print(" 클릭")
        pyautogui.click(img_capture1)
        time.sleep(5)
    except  pyautogui.ImageNotFoundException:
         print("이미지 인식 실패") 
         print(Turn)
         Turn += 1
    
         

a = click()

Turn_list = a + 1


print(a) 





        
            
         













