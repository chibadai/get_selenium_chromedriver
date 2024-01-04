# 対象のURLからjsonデータを取得
json_name = "known-good-versions-with-downloads.json"
json_url = f"https://googlechromelabs.github.io/chrome-for-testing/{json_name}"
# json_url = "http://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
print(json_url)

# 上記のURLからrequestsでjsonデータを取得
import requests

# プロトコルはhttpsで、jsonデータを取得
response = requests.get(json_url)
print(response)

# jsonデータを取得
json_data = response.json()
# print(json_data)

import datetime

now_datetime = datetime.datetime.now()
print(now_datetime)
now_datetime_str = now_datetime.strftime("%Y%m%d-%H%M%S")

import os

save_dir_json_file_path = "./data/json"
os.makedirs(save_dir_json_file_path, exist_ok=True)

# jsonファイルを保存
save_json_file_path = f"{save_dir_json_file_path}/{now_datetime_str}-{json_name}"
import json

with open(save_json_file_path, "w") as f:
    json.dump(json_data, f, indent=4)
