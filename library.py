import xml.etree.ElementTree as ET
import requests
import json
import csv

# xml parsing
# res = requests.get(
# )

# if res.status_code == 200:
#     root = ET.fromstring(res.text)
#     if root.find("error") not in root:
#         for child in root:
#             print(child.tag, child.attrib)
#     else:
#         print(root[0].text)
# else:
#     print("서버에 문제가 있습니다.", res.status_code)
# # tree = ET.parse("./learn-python/data/country.xml")

# print("[300]", "서버에 문제가 있습니다.")


# csv parsing
# 순위,서명,저자,출판사,출판년도,권,ISBN,ISBN부가기호,KDC,대출건수
with open("./learn-python/data/인기대출도서_2023-05.csv", "r", encoding="euc-kr") as f:
    reader = csv.reader(f)
    print("==================================================================================")
    print("인기대출도서")
    print("==================================================================================")
    for i, row in enumerate(reader):
        if i < 13:
            continue

        print(
            "================================================================================================="
        )
        print(
            "순위:",
            row[0],
            "서명:",
            row[1],
            "저자:",
            row[2],
            "출판사:",
            row[3],
            "출판년도:",
            row[4],
            "권:",
            row[5],
            "ISBN:",
            row[6],
            "ISBN부가기호:",
            row[7],
            "KDC:",
            row[8],
            "대출건수:",
            row[9],
        )
        print(
            "================================================================================================="
        )
