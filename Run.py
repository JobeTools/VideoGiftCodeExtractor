import os
import cv2
import pytesseract
from PIL import Image
import shutil
import json
import os
import pytesseract
from tqdm import tqdm
from threading import Thread
from math import ceil, floor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import subprocess
import sys
from pathlib import Path

from re import search

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)
num_pieces = 8
required_video_file = "OG.mp4"
my_file = Path(required_video_file)
num_pieces = int(num_pieces)
duration = get_length(required_video_file)
piece_len = duration / num_pieces
print(piece_len)
for i in range(0, num_pieces):
    starttime = floor(i * piece_len)
    endtime = ceil((i+1)*piece_len)
    ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(i)+".mp4")

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be differen

print("Video Seperation Complete")
def FE1():
    if not os.path.exists('image_frames'):
        os.makedirs('image_frames')

    test_video = cv2.VideoCapture('0.mp4')


    frameCnt = 0
    num =0
    frameRate = 50
    while True:
        ret, frame = test_video.read()
        if not ret:
            break
        if frameCnt % frameRate == 0:
           
            num = num +1
            name = './image_frames/frame'+str(int(frameCnt/frameRate))+'.png'
            cv2.imwrite(name, frame)

            
        frameCnt += 1
    test_video.release()
    cv2.destroyAllWindows()
def FE2():
    if not os.path.exists('image_frames'):
        os.makedirs('image_frames')

    test_video = cv2.VideoCapture('1.mp4')


    frameCnt = 0
    num =0
    frameRate = 50
    while True:
        ret, frame = test_video.read()
        if not ret:
            break
        if frameCnt % frameRate == 0:
        
            num = num +1
            name = './image_frames2/frame'+str(int(frameCnt/frameRate))+'.png'
            cv2.imwrite(name, frame)

            
        frameCnt += 1
    test_video.release()
    cv2.destroyAllWindows()
def FE3():
    if not os.path.exists('image_frames'):
        os.makedirs('image_frames')

    test_video = cv2.VideoCapture('2.mp4')


    frameCnt = 0
    num =0
    frameRate = 50
    while True:
        ret, frame = test_video.read()
        if not ret:
            break
        if frameCnt % frameRate == 0:
            
            num = num +1
            name = './image_frames3/frame'+str(int(frameCnt/frameRate))+'.png'
            cv2.imwrite(name, frame)

            
        frameCnt += 1
    test_video.release()
    cv2.destroyAllWindows()
def FE4():
    if not os.path.exists('image_frames'):
        os.makedirs('image_frames')

    test_video = cv2.VideoCapture('3.mp4')


    frameCnt = 0
    num =0
    frameRate = 50
    while True:
        ret, frame = test_video.read()
        if not ret:
            break
        if frameCnt % frameRate == 0:
           
            num = num +1
            name = './image_frames4/frame'+str(int(frameCnt/frameRate))+'.png'
            cv2.imwrite(name, frame)

            
        frameCnt += 1
    test_video.release()
    cv2.destroyAllWindows()
def FE5():
    if not os.path.exists('image_frames'):
        os.makedirs('image_frames')

    test_video = cv2.VideoCapture('4.mp4')


    frameCnt = 0
    num =0
    frameRate = 50
    while True:
        ret, frame = test_video.read()
        if not ret:
            break
        if frameCnt % frameRate == 0:
            
            num = num +1
            name = './image_frames5/frame'+str(int(frameCnt/frameRate))+'.png'
            cv2.imwrite(name, frame)

            
        frameCnt += 1
    test_video.release()
    cv2.destroyAllWindows()
def FE6():
    if not os.path.exists('image_frames'):
        os.makedirs('image_frames')

    test_video = cv2.VideoCapture('5.mp4')

    # Count for our frames
    frameCnt = 0
    num =0
    frameRate = 50
    while True:
        ret, frame = test_video.read()
        if not ret:
            break
        if frameCnt % frameRate == 0:
           
            num = num +1
            name = './image_frames6/frame'+str(int(frameCnt/frameRate))+'.png'
            cv2.imwrite(name, frame)

            
        frameCnt += 1
    test_video.release()
    cv2.destroyAllWindows()
def FE7():
    if not os.path.exists('image_frames'):
        os.makedirs('image_frames')

    test_video = cv2.VideoCapture('6.mp4')


    frameCnt = 0
    num =0
    frameRate = 50
    while True:
        ret, frame = test_video.read()
        if not ret:
            break
        if frameCnt % frameRate == 0:
            
            num = num +1
            name = './image_frames7/frame'+str(int(frameCnt/frameRate))+'.png'
            cv2.imwrite(name, frame)

            
        frameCnt += 1
    test_video.release()
    cv2.destroyAllWindows()
def FE8():
    if not os.path.exists('image_frames'):
        os.makedirs('image_frames')

    test_video = cv2.VideoCapture('7.mp4')


    frameCnt = 0
    num =0
    frameRate = 50
    while True:
        ret, frame = test_video.read()
        if not ret:
            break
        if frameCnt % frameRate == 0:
            
            num = num +1
            name = './image_frames8/frame'+str(int(frameCnt/frameRate))+'.png'
            cv2.imwrite(name, frame)

            
        frameCnt += 1
    test_video.release()
    cv2.destroyAllWindows()
    
f1 = Thread(target=FE1)
f2 = Thread(target=FE2)
f3 = Thread(target=FE3)
f4 = Thread(target=FE4)
f5 = Thread(target=FE5)
f6 = Thread(target=FE6)
f7 = Thread(target=FE7)
f8 = Thread(target=FE8)
f1.start()
f2.start()
f3.start()
f4.start()
f5.start()
f6.start()
f7.start()
f8.start()
f8.join()
print("\n")
print("Frame Extraction Complete")
def ET1():
    frames = os.listdir('./image_frames')
    frames.sort(key=lambda x: int(x[5:-4]))
    for frame in tqdm(frames):
        text_in_image = pytesseract.image_to_string('./image_frames/'+frame)
        text_in_image = text_in_image.replace('\n', '')
        text_in_image = text_in_image.replace('\f', '')
        text_in_image = text_in_image.strip()
        text_in_image = text_in_image.encode('ascii', 'ignore').decode()
        substring = "Code"
        if(len(text_in_image) != 0):
            if search(substring, text_in_image):
                with open('image_to_text.json', 'a') as outputFile:
                    json.dump(text_in_image, outputFile,indent=3)
                    outputFile.write('\n')

def ET2():
    frames = os.listdir('./image_frames2')
    frames.sort(key=lambda x: int(x[5:-4]))
    for frame in tqdm(frames):
        text_in_image = pytesseract.image_to_string('./image_frames2/'+frame)
        text_in_image = text_in_image.replace('\n', '')
        text_in_image = text_in_image.replace('\f', '')
        text_in_image = text_in_image.strip()
        text_in_image = text_in_image.encode('ascii', 'ignore').decode()
        substring = "Code"
        if(len(text_in_image) != 0):
            if substring in text_in_image:
                with open('image_to_text.json', 'a') as outputFile:
                    json.dump(text_in_image, outputFile,indent=3)
                    outputFile.write('\n')

def ET3():
    frames = os.listdir('./image_frames3')
    frames.sort(key=lambda x: int(x[5:-4]))

    for frame in tqdm(frames):
        text_in_image = pytesseract.image_to_string('./image_frames3/'+frame)
        text_in_image = text_in_image.replace('\n', '')
        text_in_image = text_in_image.replace('\f', '')
        text_in_image = text_in_image.strip()
        text_in_image = text_in_image.encode('ascii', 'ignore').decode()
        substring = "Code"
        if(len(text_in_image) != 0):
            if substring in text_in_image:
                with open('image_to_text.json', 'a') as outputFile:
                    json.dump(text_in_image, outputFile,indent=3)
                    outputFile.write('\n')
def ET4():
  
    frames = os.listdir('./image_frames4')
    frames.sort(key=lambda x: int(x[5:-4]))
   
    for frame in tqdm(frames):
        text_in_image = pytesseract.image_to_string('./image_frames4/'+frame)
        text_in_image = text_in_image.replace('\n', '')
        text_in_image = text_in_image.replace('\f', '')
        text_in_image = text_in_image.strip()
        text_in_image = text_in_image.encode('ascii', 'ignore').decode()
        substring = "Code"
        if(len(text_in_image) != 0):
            if substring in text_in_image:
                with open('image_to_text.json', 'a') as outputFile:
                    json.dump(text_in_image, outputFile,indent=3)
                    outputFile.write('\n')
              
def ET5():
    frames = os.listdir('./image_frames5')
    frames.sort(key=lambda x: int(x[5:-4]))
    for frame in tqdm(frames):
        text_in_image = pytesseract.image_to_string('./image_frames5/'+frame)
        text_in_image = text_in_image.replace('\n', '')
        text_in_image = text_in_image.replace('\f', '')
        text_in_image = text_in_image.strip()
        text_in_image = text_in_image.encode('ascii', 'ignore').decode()
        substring = "Code"
        if(len(text_in_image) != 0):
            if substring in text_in_image:
                with open('image_to_text.json', 'a') as outputFile:
                    json.dump(text_in_image, outputFile,indent=3)
                    outputFile.write('\n')
             
def ET6():
  
    frames = os.listdir('./image_frames6')
    frames.sort(key=lambda x: int(x[5:-4]))
    for frame in tqdm(frames):
        text_in_image = pytesseract.image_to_string('./image_frames6/'+frame)
        text_in_image = text_in_image.replace('\n', '')
        text_in_image = text_in_image.replace('\f', '')
        text_in_image = text_in_image.strip()
        text_in_image = text_in_image.encode('ascii', 'ignore').decode()
        substring = "Code"
        if(len(text_in_image) != 0):
            if substring in text_in_image:
                with open('image_to_text.json', 'a') as outputFile:
                    json.dump(text_in_image, outputFile,indent=3)
                    outputFile.write('\n')
def ET7():
    frames = os.listdir('./image_frames7')
    frames.sort(key=lambda x: int(x[5:-4]))
    for frame in tqdm(frames):
        text_in_image = pytesseract.image_to_string('./image_frames7/'+frame)
        text_in_image = text_in_image.replace('\n', '')
        text_in_image = text_in_image.replace('\f', '')
        text_in_image = text_in_image.strip()
        text_in_image = text_in_image.encode('ascii', 'ignore').decode()
        substring = "Code"
        if(len(text_in_image) != 0):
            if substring in text_in_image:
                with open('image_to_text.json', 'a') as outputFile:
                    json.dump(text_in_image, outputFile,indent=3)
                    outputFile.write('\n')

def ET8():
    frames = os.listdir('./image_frames8')
    frames.sort(key=lambda x: int(x[5:-4]))
    for frame in tqdm(frames):
        text_in_image = pytesseract.image_to_string('./image_frames8/'+frame)
        text_in_image = text_in_image.replace('\n', '')
        text_in_image = text_in_image.replace('\f', '')
        text_in_image = text_in_image.strip()
        text_in_image = text_in_image.encode('ascii', 'ignore').decode()
        substring = "Code"
        if(len(text_in_image) != 0):
            with open('image_to_text.json', 'a') as outputFile:
                json.dump(text_in_image, outputFile,indent=3)
                outputFile.write('\n')


t1 = Thread(target=ET1)
t2 = Thread(target=ET2)
t3 = Thread(target=ET3)
t4 = Thread(target=ET4)
t5 = Thread(target=ET5)
t6 = Thread(target=ET6)
t7 = Thread(target=ET7)
t8 = Thread(target=ET8)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t8.join()
print("Finshed Reading Frames Exported Text to file :)")
print("Extracting Codes From File")

import re
import json
dataLog = []
with open('image_to_text.json', 'rt') as f:
    data = f.readlines()
for line in data:
    if 'Code' in line:
        C = re.compile(r'\w{4}-\w{6}-\w{4}')
        test = C.findall(line)
        dataLog.append(test)

dataLog = list(filter(None, dataLog))
res = []
for i in dataLog:
    if i not in res:
        res.append(i)
with open('C:/Users/YOURNAME/Desktop/Codes.txt', 'w') as f: #here
    for item in res:
        str_item = str(item)
        str_item_cleaned = re.sub(r"[[\[\]\'\" ]","",str_item)
        f.write("%s\n" % str_item_cleaned)
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
num_lines = sum(1 for line in open('C:/Users/YOURNAME/Desktop/Codes.txt')) #here
with open('C:/Users/YOURNAME/Desktop/Codes.txt') as fp: #here
  fp = fp.readlines()
  for line in reversed(fp):
    code =line.strip()
    stringCode="document.getElementById('gc-redemption-input').value = '"+code+"';"
    path = r"C:\\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
    chrome_driver = path
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    driver.get("https://www.amazon.co.uk/gc/redeem")
    driver.execute_script(stringCode)
    driver.execute_script("document.getElementById('gc-redemption-apply-button').click()")
    time.sleep(1)
print("Finshed")


