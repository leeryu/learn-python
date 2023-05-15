import os  # 운영체제 관련
import shutil  # 파일 복사
import sys  # 시스템 관련
import re  # 정규 표현식
import json
import datetime

print(os.getcwd())  # 현재 디렉토리
# os.chdir("..")  # 상위 디렉토리로 이동
# os.chdir("./tutorial/data")  # 하위 디렉토리로 이동
# os.system("ls -alh")  # 시스템 명령어 호출
# print(f"tutorial access is {os.access('tutorial', os.R_OK)}")  # 파일 존재 여부 확인

# shutil.copyfile("sam", "sam2")  # 파일 복사
# for i in range(3, 10):
#     shutil.copyfile("sam", f"sam{i}")  # 파일 복사

# os.system("ls -alh")  # 시스템 명령어 호출

# for arg in enumerate(sys.argv):
#     print(arg)

question = "What is your name?"
find_strs = re.findall(r"[wW]h[a-zA-Z]+", question)  # 정규 표현식으로 단어 추출
question = re.sub(r"[wW]h[a-zA-Z]+", "Who", question)  # 정규 표현식으로 단어 치환
# print(question)
# print("tea for too".replace("too", "two", 1))

# 10.7 인터넷 액세스
from urllib.request import urlopen

# with urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt") as response:
#     # print(response.read().decode("utf-8"))
#     for line in response:
#         line = line.decode("utf-8")
#         if line.startswith("datetime"):
#             print(line.rstrip())
# datetime: 2023-03-22T13:01:07.404270+00:00

# 10.8 날짜와 시간
# from datetime import date, time, datetime, timedelta

# now = date.today()
# birthday = date(1984, 1, 30)

# age = now - birthday
# print(age)
# print(age.days / 365)

# 10.10 성능 측정
from timeit import Timer

print(Timer("t=a; a=b; b=t", "a=1; b=2").timeit())
