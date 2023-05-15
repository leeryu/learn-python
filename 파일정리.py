import os
import shutil
import datetime
import sys

args = sys.argv

if len(args) < 2:
    print("파일 경로를 입력해주세요.")
    sys.exit()

path = args[1]


def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y%m")
        return True
    except ValueError:
        return False


# sam_20221102
ignored_file_list = []

try:
    files = os.listdir(path)
except Exception as e:
    print("파일 경로를 확인해주세요.")
    sys.exit()

for f in files:
    try:
        file_name = f.split("_")

        if len(file_name) < 2:
            ignored_file_list.append(f)
            continue

        directory_name = file_name[1][:6]

        if validate_date(directory_name) == False:
            ignored_file_list.append(f)
            continue

        isExist = os.path.exists(path + directory_name)

        if isExist == False:
            os.makedirs(path + directory_name)

        shutil.move(path + f, path + directory_name + "/" + f)
    except Exception as e:
        ignored_file_list.append(f)
        print(e)


print("ignored_file_list: ", ignored_file_list)

print(datetime.datetime.strptime("202332", "%Y%m"))
