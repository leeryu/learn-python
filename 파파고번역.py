import requests
import sys
import json

url = "https://openapi.naver.com/v1/papago/n2mt"


def get_translated_text(text, source, target):
    json_obj = call(
        url,
        headers={
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Naver-Client-Id": "",
            "X-Naver-Client-Secret": "",
        },
        params={"source": source, "target": target, "text": text},
    )

    return json_obj["message"]["result"]["translatedText"]


def call(url, headers, params):
    response = requests.post(url, headers=headers, params=params)

    json_obj = response.json()
    json_formatted_str = json.dumps(json_obj, indent=4)
    print(json_formatted_str)

    return json_obj


args = sys.argv

if len(args) < 2:
    print("번역할 텍스트를 입력해주세요.")
    sys.exit()

text = args[1]

translated_text = get_translated_text(text, "ko", "en")

print(f"번역된 텍스트: {translated_text}")
